import os
import markdown2
from flask import Flask, render_template, request, redirect, url_for, session
from openai import OpenAI

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong random secret in production

# ── OpenAI client ──────────────────────────────────────────────
# Set the key in your OS environment before running:
#   Linux/Mac:  export OPENAI_API_KEY="sk-..."
#   Windows:    set OPENAI_API_KEY=sk-...
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = (
    "You are a helpful, friendly AI assistant. "
    "Answer the user's questions clearly and concisely."
)


def ask_openai(user_message: str, history: list) -> str:
    """
    Send the full conversation history + new user message to OpenAI
    and return the assistant's reply as a string.
    """
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)                          # past turns
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # cheap & fast; swap for "gpt-4o" if you want
        messages=messages,
        max_tokens=1024,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()


# ── Login ──────────────────────────────────────────────────────
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            session['history'] = []   # fresh conversation on every login
            return redirect(url_for('home'))
        else:
            return render_template('index.html', error="Invalid username or password")

    return render_template('index.html')


# ── Home / Chat ────────────────────────────────────────────────
@app.route('/home', methods=['GET', 'POST'])
def home():
    if not session.get('logged_in'):
        return redirect(url_for('index'))

    user_input = None
    ai_response = None
    error = None

    if request.method == 'POST':
        user_input = request.form.get('user_input', '').strip()

        if user_input:
            history = session.get('history', [])

            try:
                ai_response_raw = ask_openai(user_input, history)

                # Convert Markdown → HTML for clean rendering in the UI
                ai_response = markdown2.markdown(
                    ai_response_raw,
                    extras=["fenced-code-blocks", "tables", "strike", "break-on-newline"]
                )

                # Store raw text for OpenAI context, HTML for display
                history.append({"role": "user",      "content": user_input})
                history.append({"role": "assistant", "content": ai_response_raw, "html": ai_response})

                # Keep last 20 messages (10 turns) to avoid token overflow
                session['history'] = history[-20:]

            except Exception as e:
                error = f"OpenAI error: {str(e)}"

    return render_template(
        'home.html',
        user_input=user_input,
        ai_response=ai_response,
        history=session.get('history', []),
        error=error,
    )


# ── Logout ─────────────────────────────────────────────────────
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5015, host='0.0.0.0')