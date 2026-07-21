from datetime import datetime


def validate_name(name):

    name = name.strip()

    if not name:
        return False, "Name cannot be empty"

    if len(name) < 2 :
        return False, "Name cannot be less than 2 characters"

    if not all(char.isalpha() or char.isspace() for char in name):
        return False, "Name should contain only letters and spaces"

    if len(name) > 20:
        return False, "Name cannot exceed 20 characters"

    return True, "Valid Name"

def validate_email(email):
    email = email.strip()

    if not email:
        return False, "Email cannot be empty"
    if not '@' in email:
        return False, "Invalid Email(add @)"
    if not '.' in email:
        return False, "Invalid Email(add . )"

    at_index = email.index('@')
    dot_index = email.rfind('.')
    if email.startswith('@') or email.startswith('.'):
        return False, "Invalid Email"

    if dot_index < at_index:
        return False, "'.' must come after '@'"
    if email.endswith('@') or email.endswith('.'):
        return False, "Invalid Email"
    if email.count('@') != 1:
        return False, "Email must contain exactly one @"
    if email.endswith('@gmail.com'):
        return True, "Valid Email"
    
    return True, "Valid Email"

    
 
def validate_phone(phone):
    phone = phone.strip()
    if len(phone) != 10:
        return False, "Phone number must contain exactly 10 digits"
    if not phone.isdigit():
        return False, "Phone No. Can Only be Number" 
    return True, "Valid Phone Number"



def validate_password(password):
    password = password.strip()
    special = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

    if not any(c in special for c in password):
        return False, "Password must contain at least one special character"
    if not password:
        return False, "Password cannot be empty"
    if len(password) < 8:
        return False, "Password minimum 8 digit"
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter"
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter"
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one Numbers"
    
    return True, "Valid Password"

def validate_age(age):
    if age < 18 or age > 100:
        return False, "Age cannot be less than 18 and greater than 100 "

def validate_flight_number(flight_number):

    flight_number = flight_number.strip()

    if not flight_number:
        return False, "Flight number cannot be empty"

    if len(flight_number) < 5 or len(flight_number) > 7:
        return False, "Flight number must be between 5 and 7 characters"

    letters = ""
    numbers = ""

    for char in flight_number:
        if char.isalpha():
            letters += char
        elif char.isdigit():
            numbers += char
        else:
            return False, "Flight number can only contain letters and numbers"

    if not letters.isupper():
        return False, "Airline code must be uppercase"

    if len(letters) < 2 or len(letters) > 3:
        return False, "Airline code must contain 2 or 3 letters"

    if len(numbers) < 3 or len(numbers) > 4:
        return False, "Flight number must contain 3 or 4 digits"

    return True, "Valid Flight Number"

def validate_airport_code(airport_code):
    airport_code = airport_code.strip()

    if not airport_code.isalpha():
        return False, "Airport code must be uppercase"
    if len(airport_code) != 3:
        return False, "Airport code must contain 3 letters"
    return True, "Valid Airport Code"


def validate_price(price):
    price = float(price)

    if price < 0:
        return False, "Price Should Greater than 0"
    
    return True, "Valid Price"

def validate_seats(seats):
    if seats == 0:
        return False, "Seat Should Greater than 0"
    
    return True, "Valid Seat"



def validate_date(date):
    date = date.strip()

    if not date:
        return False, "Date cannot be empty"

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True, "Valid Date"
    except ValueError:
        return False, "Invalid Date (Use YYYY-MM-DD)"


def validate_time(time):
    time = time.strip()

    if not time:
        return False, "Time cannot be empty"

    try:
        datetime.strptime(time, "%H:%M")
        return True, "Valid Time"
    except ValueError:
        return False, "Invalid Time (Use HH:MM)"
    
def validate_menu_choice(menu_choice):
    menu_choice = menu_choice.strip()
    if not menu_choice.isdigit():
        return False, "Invalid Choice"
    if int(menu_choice) not in range(1,8):
        return False, "Invalid Choice"
    return True, "Valid Choice"
    

def validate_yes_no(yes_no):
    if yes_no in ("y","yes","n","no"):
        return True,"Valid Choice"

    return False,"Enter Yes/No"
