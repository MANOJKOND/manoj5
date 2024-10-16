from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='database-1.ctw02s8ycvdb.ap-south-1.rds.amazonaws.com',  # e.g., 'localhost' or your RDS endpoint
        user='admin',
        password='kondamanoj9989',
        database='database-1'
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)', (username, email, password))
    conn.commit()

    cursor.close()
    conn.close()
    
    return redirect('/')  # Redirect to home after registration

if __name__ == '__main__':
    app.run(debug=True)
