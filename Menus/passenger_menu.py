from Services.booking_service import Book_seat
from Services.booking_service import Cancel_booking
from Services.booking_service import Booking_history
from Services.flight_service import Search_flights
from Services.flight_service import View_flights
from Services.payment_service import Payments_menu

def passenger_dashboard():
    while True:
        print("======================== PASSENGER DASHBOARD ========================")
        print("1. Search Flights")
        print("2. View Flights")
        print("3. Book Ticket")
        print("4. Cancel Ticket")
        print("5. Booking History")
        print("6. Payments")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            Search_flights()
        elif choice == '2':
            View_flights()
        elif choice == '3':
            Book_seat()
        elif choice == '4':
            Cancel_booking()
        elif choice == '5':
            Booking_history()
        elif choice == '6':
            Payments_menu()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

