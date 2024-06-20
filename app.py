import re
import bleach
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="DB_USERNAM",   # Replace with your MySQL username
    password="DB_PASSWORD",   # Replace with your MySQL password
    database="flask_data"    # Replace with your MySQL database name
)
cursor = db.cursor()

# Sanitize html with bleach
def sanitize_input(input):
    return bleach.clean(input)

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_name(name):
    pattern = r'^[a-zA-Z\s-]+$'
    return re.match(pattern, name) is not None

def is_valid_message(message):
    return len(message) > 0

countries = ["Belgium", "France", "Luxembourg", "Germany"]

@app.route('/')
def index():
    return render_template('index.html', countries=countries)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        
        first_name = sanitize_input(request.form['first_name'])
        last_name = sanitize_input(request.form['last_name'])
        email = sanitize_input(request.form['email'])
        country = sanitize_input(request.form['country'])
        message = sanitize_input(request.form['message'])
        gender = sanitize_input(request.form['gender'])
        subjects = ",".join(request.form.getlist('subjects[]'))
        honeypot = request.form.get('honeypot')

        # Checking if the honeypot has been filled
        if honeypot:
            return render_template('index.html', error_message="Form submission rejected.", countries=countries, 
                                   first_name=first_name, last_name=last_name, email=email, message=message)

        # Checking if every field has been filled
        if not (first_name and last_name and email and country and message and gender):
            error_message = "All form fields are required."
            return render_template('index.html', error_message=error_message, countries=countries, 
                                   first_name=first_name, last_name=last_name, email=email, message=message)

        # Validating Email
        if not is_valid_email(email):
            error_message = "Invalid email address."
            return render_template('index.html', error_message=error_message, countries=countries, 
                                   first_name=first_name, last_name=last_name, email=email, message=message)

        # Validating Name
        if not is_valid_name(first_name) or not is_valid_name(last_name):
            error_message = "Invalid characters in name."
            return render_template('index.html', error_message=error_message, countries=countries, 
                                   first_name=first_name, last_name=last_name, email=email, message=message)

        # Validate Message
        if not is_valid_message(message):
            error_message = "Message cannot be empty."
            return render_template('index.html', error_message=error_message, countries=countries, 
                                   first_name=first_name, last_name=last_name, email=email, message=message)

        # Inserting data into MySQL
        insert_query = "INSERT INTO submissions (first_name, last_name, email, country, message, gender, subjects) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, email, country, message, gender, subjects)
        cursor.execute(insert_query, values)
        db.commit()

        # if all inputs are validated
        return redirect(url_for('success', first_name=first_name, last_name=last_name, email=email, 
                                country=country, message=message, gender=gender, subjects=subjects))

@app.route('/success')
def success():
    return render_template('success.html', 
                           first_name=request.args.get('first_name'),
                           last_name=request.args.get('last_name'),
                           email=request.args.get('email'),
                           country=request.args.get('country'),
                           message=request.args.get('message'),
                           gender=request.args.get('gender'),
                           subjects=request.args.get('subjects').split(','))

if __name__ == '__main__':
    app.run(debug=True)
