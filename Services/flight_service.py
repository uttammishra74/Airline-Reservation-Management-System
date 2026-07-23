import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from datetime import date
from Database.connection import get_connection
from Utils.validators import (
    validate_flight_number,
    validate_date,
    validate_price,
    validate_seats,
    validate_time,
    validate_menu_choice,
    validate_airport_code
)



def Add_flight():

    flight_number = input("Flight number: ").strip()
    valid, message = validate_flight_number(flight_number)
    if not valid:
        print(message)
        return
    
    airline_name = input("Airline Name : ")

    source_airport = input("Source Airport ID : ")
    valid, message = validate_airport_code(source_airport)
    if not valid:
        print(message)
        return

    today = date.today().strftime("%Y-%m-%d")

    departure_time_input = input("Departure Time (HH:MM): ").strip()
    valid, message = validate_time(departure_time_input)
    if not valid:
        print(message)
        return
    departure_time = f"{today} {departure_time_input}:00"

    arrival_time_input = input("Arrival Time (HH:MM): ").strip()
    valid, message = validate_time(arrival_time_input)
    if not valid:
        print(message)
        return
    arrival_time = f"{today} {arrival_time_input}:00"


    economy_seats = int(input("Economy Seats : "))
    valid, message = validate_seats(economy_seats)
    if not valid:
        print(message)
        return

    business_seats = int(input("Business Seats : "))
    valid, message = validate_seats(business_seats)
    if not valid:
        print(message)
        return
    
    economy_price = input("Economy Price : ")
    valid, message = validate_price(economy_price)
    if not valid:
        print(message)
        return

    business_price= input("Business Price : ")
    valid, message = validate_price(business_price)
    if not valid:
        print(message)
        return

    status = input("Status [Scheduled/Delayed/Cancelled]: ").strip().title()
    if status == "":
        status = "Scheduled"

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        INSERT INTO flights (
            flight_number, airline_name, source_airport, 
            departure_time, arrival_time, economy_seats, business_seats, 
            economy_price, business_price, status
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (
                flight_number,
                airline_name,
                source_airport,
                departure_time,
                arrival_time,
                economy_seats,
                business_seats,
                economy_price,
                business_price,
                status,
            ),
        )
        connection.commit()

    except Exception as error:
        print(f"Adding Flight failed: {error}")
        connection.rollback()
        return

    finally:
        cursor.close()  
        connection.close()  

    print("Flight Added Successful!")


def Delete_flight():
    flight_number = input("Flight No. : ")
    airline_name = input("Airline Name : ")

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        DELETE FROM flights 
        WHERE flight_number = %s AND airline_name = %s;
        """
        cursor.execute(
            query,
            (
                flight_number,
                airline_name
            ),
        )
        connection.commit()

        if cursor.rowcount == 0:
            print("No matching flight found to delete.")
        else:
            connection.commit()
            print("Flight Delete Successful!")

    except Exception as error:
        print(f"Deletion failed: {error}")
        connection.rollback()
        return

    finally:
        cursor.close()  
        connection.close()  

    print("Flight Delete Successful!")
      


def Update_flight():
    print("Enter The Flight Details You Want To Update")
    flight_number = input("Flight No. : ").strip()
    airline_name = input("Airline Name : ").strip()

    connection = get_connection()
    cursor = connection.cursor()
    
    query = """
        SELECT 1 FROM flights WHERE flight_number = %s AND airline_name = %s LIMIT 1
    """
    cursor.execute(query, (flight_number, airline_name))
    flight_exists = cursor.fetchone()

    if flight_exists:
        print("\n--- Update Your Flight Info ---")
        update_flight_number = input("New Flight number : ").strip()
        valid, message = validate_flight_number(update_flight_number)
        if not valid:
            print(message)
            cursor.close()
            connection.close()
            return
        
        update_airline_name = input("New Airline Name : ").strip()
    
        source_airport = input("Source Airport ID : ").strip()
        valid, message = validate_airport_code(source_airport)
        if not valid:
            print(message)
            cursor.close()
            connection.close()
            return
    
        today = date.today().strftime("%Y-%m-%d")
    
        departure_time_input = input("Departure Time (HH:MM): ").strip()
        valid, message = validate_time(departure_time_input)
        if not valid:
            print(message)
            cursor.close()
            connection.close()
            return
        departure_time = f"{today} {departure_time_input}:00"
    
        arrival_time_input = input("Arrival Time (HH:MM): ").strip()
        valid, message = validate_time(arrival_time_input)
        if not valid:
            print(message)
            cursor.close()
            connection.close()
            return
        arrival_time = f"{today} {arrival_time_input}:00"
    
        economy_seats = int(input("Economy Seats : "))
        valid, message = validate_seats(economy_seats)
        if not valid:
            print(message)
            cursor.close()
            connection.close()
            return
    
        business_seats = int(input("Business Seats : "))
        valid, message = validate_seats(business_seats)
        if not valid:
            print(message)
            cursor.close()
            connection.close()
            return
        
        economy_price = input("Economy Price : ")
        valid, message = validate_price(economy_price)
        if not valid:
            print(message)
            cursor.close()
            connection.close()
            return
    
        business_price = input("Business Price : ")
        valid, message = validate_price(business_price)
        if not valid:
            print(message)
            cursor.close()
            connection.close()
            return
    
        status = input("Status [Scheduled/Delayed/Cancelled]: ").strip().title()
        if status == "":
            status = "Scheduled"
        
        try:
            query = """
                UPDATE flights 
                SET 
                    flight_number = %s,
                    airline_name = %s,
                    source_airport = %s,  
                    departure_time = %s, 
                    arrival_time = %s, 
                    economy_seats = %s, 
                    business_seats = %s, 
                    economy_price = %s, 
                    business_price = %s, 
                    status = %s
                WHERE flight_number = %s AND airline_name = %s
            """
    

            cursor.execute(
                query,
                (
                    update_flight_number,
                    update_airline_name, 
                    source_airport,      
                    departure_time,      
                    arrival_time,        
                    economy_seats,       
                    business_seats,      
                    economy_price,       
                    business_price,      
                    status,
                    flight_number,
                    airline_name  
                ),
            )
            connection.commit()
            print("Flight Update Successful!")
    
        except Exception as error:
            print(f"Updating Flight failed: {error}")
            connection.rollback()
            return
    
        finally:
            cursor.close()  
            connection.close()  

    else:
        print("❌ Error: This flight number and airline combination does not exist.")
        cursor.close()
        connection.close()
        return




def Search_flights():

    print("Enter The Flight Details You Want To Search")
    flight_number = input("Flight No. : ")
    airline_name = input("Airline Name : ")

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT * FROM flights WHERE flight_number = %s AND airline_name = %s
        """

        cursor.execute(
            query,
            (
                flight_number,
                airline_name,
            ),
        )

        flight = cursor.fetchone()
        
        if flight:
            print("\n--- Flight Details Found ---")
            for column, value in flight.items():
                print(f"{column.replace('_', ' ').title()}: {value}")
        else:
            print("\nNo flight found with those details.")

    except Exception as error:
            print(f"Searching Flight failed: {error}")
            return
    
    finally:
            cursor.close()  
            connection.close()
    

def View_flights():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    
    try:
        query = """
            SELECT * FROM flights
        """
        cursor.execute(query)

        flights = cursor.fetchall()
        
        if flights:
            print("\n================ AVAILABLE FLIGHTS ================")

            for flight in flights:
                print(f"\n✈️ Flight: {flight.get('flight_number')} | {flight.get('airline_name')}")
                print("-" * 40)
                
                for column, value in flight.items():
                    print(f"  {column.replace('_', ' ').title()}: {value}")
            print("\n===================================================")
        else:
            print("\n❌ No flights found in the database.")

    except Exception as error:
        print(f"Viewing Flight failed: {error}")
        return
    
    finally:
        cursor.close()  
        connection.close()



def flights_menu():
    while True:
        print("\n1. Add Flight")
        print("2. Delete Flight")
        print("3. Update Flight")
        print("4. Search Flight")
        print("5. View Flight")
        print("6. Exit")

        choice = input("Choose: ")

        valid, message = validate_menu_choice(choice)
        if not valid:
            print(message)
            return

        if choice == "1":
            Add_flight()
        elif choice == "2":
            Delete_flight()
        elif choice == "3":
            Update_flight()
        elif choice == "4":
            Search_flights()
        elif choice == "5":
            View_flights()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
            
flights_menu()




