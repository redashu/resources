from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

def try_db_connection(user, password):
    host = os.getenv('MYSQL_HOST')
    
    if not host:
        raise EnvironmentError("Missing required environment variable: MYSQL_HOST")
    
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        connection.close()
        return True
    except mysql.connector.Error:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if try_db_connection(username, password):
        return render_template('success.html', message="Login successful!")
    else:
        return render_template('index.html', error="Invalid username or password")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
