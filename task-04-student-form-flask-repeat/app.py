from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret_key'  # Needed for flash messages

students_data = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    age = request.form.get('age')
    dob = request.form.get('dob')
    gender = request.form.get('gender')
    course = request.form.get('course')
    mark1 = request.form.get('mark1')
    mark2 = request.form.get('mark2')
    total = request.form.get('total')
    address = request.form.get('address')

    # Server-side validations
    errors = []

    # Name validation
    if not name or len(name) < 3:
        errors.append('Name must be at least 3 characters')

    # Email validation
    if not email or '@' not in email:
        errors.append('Invalid email address')

    # Phone validation
    if not phone or len(phone) != 10 or not phone.isdigit():
        errors.append('Phone must be 10 digits')

    # Age validation

    # Gender validation
    if not gender:
        errors.append('Please select gender')

    # Course validation
    if not course:
        errors.append('Please select a course')

    # Address validation
    if not address or len(address) < 10:
        errors.append('Address must be at least 10 characters')

    # If there are errors, show them
    if errors:
        for error in errors:
            flash(error, 'danger')
        return redirect(url_for('home'))

    # If no errors, save data
    student = {
        'name': name,
        'email': email,
        'phone': phone,
        'age': age,
        'dob': dob,
        'gender': gender,
        'course': course,
        'mark1': mark1,
        'mark2': mark2,
        'total': total,
        'address': address,
    }

    students_data.append(student)
    flash('Student registered successfully!', 'success')
    return redirect(url_for('display'))

@app.route('/display')
def display():
    return render_template('display.html', students=students_data)

if __name__ == '__main__':
    app.run(debug=True)
