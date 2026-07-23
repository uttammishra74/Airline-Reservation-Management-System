import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from Database.connection import get_connection
from Utils.validators import (
    validate_booking_id,
    validate_menu_choice
)


def Book_seat():

    passenger_id = input("Passenger ID : ")
    valid, message = validate_booking_id(passenger_id)
    if not valid:
        print(message)
        return

    seat_class = input("Seat Class (Economy, Business) : ")
    if seat_class == "":
        seat_class = "Economy"
    elif seat_class not in ["economy", "business"]:
        print("Invalid Class! Please type Economy or Business.")
        return

    seat_booked = input("How many seats you want to book : ")

    if not seat_booked.isdigit():
        print("Seat Can only be number : ")
    else:
        seat_booked = int(seat_booked)
        
        if 1 <= seat_booked <= 15:
            print(f"Success! You booked the number: {seat_booked}")
        else:
            print("Error: You can only book a number from 1 to 15. Try again.")


    connection = get_connection()
    cursor = connection.cursor()

    total_amount = 0
    while True:
        flight_number = input("Flight number: ").strip()

        try:
                if seat_class == "Economy":
                    query = "SELECT economy_price FROM flights WHERE flight_number = %s"
                else:
                    query = "SELECT business_price FROM flights WHERE flight_number = %s"
                    
                cursor.execute(query, [flight_number])
                result = cursor.fetchone()
                
                if not result:
                    print("Please enter the correct flight number.")
                    continue
                if result :
                    old_flight_id = flight_number

                ticket_price = result[0]
                total_amount = ticket_price * seat_booked
                print(f"Your Total amount is {total_amount}.00")
                break

        
        except Exception as error:
            print(f"Booking Ticket Failed: {error}")
            connection.rollback()
            return


    status = input("Status [Confirmed/Cancelled]: ").strip().title()
    if status == "":
        status = "Confirmed"


    try:
        query = """
        INSERT INTO bookings (
            passenger_id,flight_number,seat_class,seats_booked,total_amount,booking_status
        ) VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (
                passenger_id,
                old_flight_id,
                seat_class,
                seat_booked,
                total_amount,
                status
            ),
        )
        connection.commit()

    except Exception as error:
        print(f"Booking Ticket failed: {error}")
        connection.rollback()
        return

    finally:
        cursor.close()  
        connection.close()  

    print("Ticket Booked Successful!")

def Cancel_booking():
    passenger_id = input("Passenger id : ")
    flight_number = input("Flight number : ")

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        UPDATE bookings 
                SET booking_status = 'Cancelled' 
                WHERE passenger_id = %s 
                AND flight_number = %s;

        """
        cursor.execute(
            query,
            (
                passenger_id,
                flight_number
            ),
        )

        if cursor.rowcount == 0:
            print("No matching booking found to cancel.")
        else:
            connection.commit()
            print("Booking Cancelled Successful!")

    except Exception as error:
        print(f"Cancellion failed: {error}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()

def Booking_history():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    
    try:
        query = """
            SELECT * FROM bookings
        """
        cursor.execute(query)

        history = cursor.fetchall()
        
        if history:
            print("\n================ Booking History ================")

            for hstry in history:
                print(f"\n✈️")
                print("-" * 40)
                
                for column, value in hstry.items():
                    print(f"  {column.replace('_', ' ').title()}: {value}")
            print("\n===================================================")
        else:
            print("\n❌ No history found in the database.")

    except Exception as error:
        print(f"Booking history failed: {error}")
        return
    
    finally:
        cursor.close()  
        connection.close()

# def Booking_menu():
#     while True:
#         print("\n1. Booking Seat")
#         print("2. Cancel Booking")
#         print("3. Booking History")
#         print("4. Exit")


#         choice = input("Choose: ")

#         valid, message = validate_menu_choice(choice)
#         if not valid:
#             print(message)
#             return

#         if choice == "1":
#             Book_seat()
#         elif choice == "2":
#             Cancel_booking()
#         elif choice == "3":
#             Booking_history()
#         elif choice == "4":
#             break
#         else:
#             print("Invalid choice.")

# Booking_menu()
