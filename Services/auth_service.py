import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from Database.connection import get_connection
from Utils.validators import validate_email
from Utils.validators import validate_name
from Utils.validators import validate_password
from Utils.validators import validate_phone
from Utils.validators import validate_menu_choice


def register():
    print("\n===== Register =====")

    name = input("Name : ")

    valid, message = validate_name(name)
    if not valid:
        print(message)
        return

    phone = input("Phone : ").strip()

    valid, message = validate_phone(phone)
    if not valid:
        print(message)
        return

    email = input("Email : ")

    valid, message = validate_email(email)
    if not valid:
        print(message)
        return

    password = input("Password : ")

    valid, message = validate_password(password)
    if not valid:
        print(message)
        return

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        INSERT INTO passengers (full_name, email, phone, password)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, email, phone, password))
        connection.commit()
    except Exception as error:
        connection.rollback()
        if getattr(error, "errno", None) == 1062:
            print("Email already registered.")
        else:
            print(f"Registration failed: {error}")
        return
    finally:
        cursor.close()
        connection.close()

    print("Registration Successful!")



def login():
    email = input("Enter Email : ")
    password = input("Enter Password : ")

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
        SELECT *
        FROM passengers
        WHERE email = %s
        AND password = %s
        """

        cursor.execute(query, (email, password))
        user = cursor.fetchone()
    finally:
        cursor.close()
        connection.close()

    if user:
        print(f"\nWelcome {user['full_name']}!")
        return user

    else:
        print("\nInvalid Email or Password")
        return None
    

def auth_menu():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        valid, message = validate_menu_choice(choice)
        if not valid:
            print(message)
            return

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    auth_menu()
