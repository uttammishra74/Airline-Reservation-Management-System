from Services.auth_service import register
from Services.auth_service import login
from Services.auth_service import admin_login




def main_menu():
    while True:
        print("\n" + "="*28 + " AIRLINE RESERVATION SYSTEM " + "="*28)
        print("1. Register")
        print("2. Login")
        print("3. Admin Login")
        print("4. Exit")
        
        choice = input("Choose: ").strip()
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            admin_login()
        elif choice == '4':
            print("\nThank you for using our Airline Reservation System. Goodbye!")
            break
        else:
            print("\n[Invalid choice! Please select a valid option (1-4).]")