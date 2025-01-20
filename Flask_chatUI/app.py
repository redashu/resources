from flask import Flask, render_template, request, redirect, url_for,session
app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Secret key for session management
# Route for Login Page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Example: Hardcoded credentials
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True  # Set session variable
            return redirect(url_for('home'))
        else:
            error = "Invalid username or password"
            return render_template('index.html', error=error)

    return render_template('index.html')  # Render login page for GET request

# Route for the Home Page
@app.route('/home', methods=['GET', 'POST'])
def home():
    if not session.get('logged_in'):  # Check if the user is logged in
        return redirect(url_for('index'))  # Redirect to login page if not logged in
    my_input = None
    if request.method == 'POST':  # Handle form submission
        my_input = request.form.get('user_input')  # Get the text from the textarea
        
    # Render the page for GET requests or if no valid response is returned.
    return render_template('home.html', user_input=my_input)

# Route for Logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)  # Remove session variable
    return redirect(url_for('index'))

if __name__ == '__main__': 
    app.run(debug=True,port=5015)
