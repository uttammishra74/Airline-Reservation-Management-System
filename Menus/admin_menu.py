from Services.booking_service import Booking_history
from Services.flight_service import Add_flight
from Services.flight_service import Delete_flight
from Services.flight_service import Update_flight
from Services.flight_service import View_flights



def admin_dashboard():
    while True:
        print("======================== ADMIN DASHBOARD ========================")
        print("1. Add Flights")
        print("2. Update Flights")
        print("3. Delete Flight")
        print("4. Booking History")
        print("5. View Flights")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            Add_flight()
        elif choice == '2':
            Update_flight()
        elif choice == '3':
            Delete_flight()
        elif choice == '4':
            Booking_history()
        elif choice == '5':
            View_flights()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

