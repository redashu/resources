from flask import Flask, render_template, request, redirect, url_for,flash,jsonify,session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Redhat@12345'
app.config['MYSQL_DB'] = 'userdb'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_details WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        print(session.get('_flashes'))  # Debug print statement
        return render_template('dashboard.html', username=session['username'])
    else:
        flash('Please login to access this page.', 'danger')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/chart-data')
def chart_data():
    # Example data, replace with your database query
    data = {
        'labels': ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        'datasets': [{
            'label': '# of Votes',
            'data': [12, 19, 3, 5, 2, 3],
            'backgroundColor': [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            'borderColor': [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            'borderWidth': 1
        }]
    }
    return jsonify(data)

# adding training database 
@app.route('/add_training', methods=['POST'])
def add_training():
    if 'loggedin' in session:
        training_name = request.form['training_name']
        technology = request.form['technology']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        vendor = request.form['vendor']
        company_name = request.form['company_name']
        remarks = request.form['remarks']
        labs_used = request.form['labs_used']
        
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO training_details (training_name, technology, start_date, end_date, vendor, company_name, remarks, labs_used) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', 
                           (training_name, technology, start_date, end_date, vendor, company_name, remarks, labs_used))
            mysql.connection.commit()
            cursor.close()
            flash('Training added successfully!', 'success')
        except Exception as e:
            flash('Failed to add training. Please try again.', 'danger')
        
        return redirect(url_for('dashboard'))
    else:
        flash('Please login to access this page.', 'danger')
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True,port=8081,host='0.0.0.0')