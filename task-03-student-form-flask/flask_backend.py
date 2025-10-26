from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime, date
import secrets
import re

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generate secure secret key

# In-memory storage (use database in production)
students_data = {}

def calculate_age(birthdate_str):
    """Calculate age from birthdate string"""
    try:
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
        today = date.today()
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        return age
    except:
        return None

def validate_form_data(data):
    """Validate form data on server side"""
    errors = []
    
    # Validate name
    name = data.get('name', '').strip()
    if not name or len(name) < 3:
        errors.append('Name must be at least 3 characters')
    if not re.match(r'^[A-Za-z\s]+$', name):
        errors.append('Name can only contain letters and spaces')
    
    # Validate email
    email = data.get('email', '').strip()
    email_pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    if not email or not re.match(email_pattern, email):
        errors.append('Invalid email address')
    
    # Validate birthdate
    birthdate = data.get('birthdate')
    if not birthdate:
        errors.append('Birthdate is required')
    else:
        try:
            birth_date = datetime.strptime(birthdate, '%Y-%m-%d').date()
            if birth_date > date.today():
                errors.append('Birthdate cannot be in the future')
        except:
            errors.append('Invalid birthdate format')
    
    # Validate program
    program = data.get('program')
    valid_programs = ['Computer Science', 'Engineering', 'Business Administration', 
                     'Arts & Humanities', 'Natural Sciences']
    if not program or program not in valid_programs:
        errors.append('Please select a valid program')
    
    # Validate marks
    try:
        marks1 = float(data.get('marks1', 0))
        if marks1 < 0 or marks1 > 100:
            errors.append('Marks 1 must be between 0 and 100')
    except:
        errors.append('Invalid marks 1')
    
    try:
        marks2 = float(data.get('marks2', 0))
        if marks2 < 0 or marks2 > 100:
            errors.append('Marks 2 must be between 0 and 100')
    except:
        errors.append('Invalid marks 2')
    
    return errors

@app.route('/')
def index():
    """Display registration form"""
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    """Handle form submission"""
    # Get form data
    form_data = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'birthdate': request.form.get('birthdate'),
        'program': request.form.get('program'),
        'marks1': request.form.get('marks1'),
        'marks2': request.form.get('marks2'),
        'comments': request.form.get('comments', '')
    }
    
    # Validate data
    errors = validate_form_data(form_data)
    if errors:
        for error in errors:
            flash(error, 'danger')
        return redirect(url_for('index'))
    
    # Calculate additional data
    age = calculate_age(form_data['birthdate'])
    marks1 = float(form_data['marks1'])
    marks2 = float(form_data['marks2'])
    total = marks1 + marks2
    average = total / 2
    
    # Create student record
    student_id = secrets.token_urlsafe(16)
    student_record = {
        'id': student_id,
        'name': form_data['name'],
        'email': form_data['email'],
        'birthdate': form_data['birthdate'],
        'age': age,
        'program': form_data['program'],
        'marks1': marks1,
        'marks2': marks2,
        'total': total,
        'average': average,
        'comments': form_data['comments'],
        'submitted_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Store in memory (use database in production)
    students_data[student_id] = student_record
    
    # Store student ID in session
    session['student_id'] = student_id
    
    flash('Registration successful!', 'success')
    return redirect(url_for('display'))

@app.route('/display')
def display():
    """Display student details"""
    student_id = session.get('student_id')
    
    if not student_id or student_id not in students_data:
        flash('No student data found. Please submit the form first.', 'warning')
        return redirect(url_for('index'))
    
    student = students_data[student_id]
    return render_template('display.html', student=student)

@app.route('/clear')
def clear():
    """Clear session data"""
    student_id = session.get('student_id')
    if student_id and student_id in students_data:
        del students_data[student_id]
    session.clear()
    flash('Data cleared successfully!', 'info')
    return redirect(url_for('index'))

@app.route('/all-students')
def all_students():
    """View all registered students (admin view)"""
    return render_template('all_students.html', students=students_data.values())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)