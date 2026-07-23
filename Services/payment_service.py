import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from Database.connection import get_connection
from Utils.validators import (
    validate_booking_ids,
    validate_menu_choice,
    validate_payment_id,
)


def Create_payment():


    booking_id = input("Booking id : ")
    valid, message = validate_booking_ids(booking_id)
    if not valid:
        print(message)
        return
    
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT EXISTS(SELECT 1 FROM bookings WHERE booking_id = %s)"
    cursor.execute(query, (booking_id,))


    id_exists = cursor.fetchone()

    if not id_exists:
        print("Booking ID not exists.")
        cursor.close()
        connection.close()
        return



    payment_method = input("Payment - [Card,UPI,NetBanking] : ")
    if payment_method not in ["card", "upi", "netbanking"]:
            print("Invalid Class! Please type Card, UPI or NetBanking.")
            return


    total_amount = 0
    while True:  
        try:
            query = "SELECT total_amount FROM bookings WHERE booking_id = %s"
            cursor.execute(query, [booking_id])
            result = cursor.fetchone()              
            ticket_price = result[0]
            total_amount = ticket_price
            print(f"Your Total amount is {total_amount}.00")
            total = total_amount
            break

    
        except Exception as error:
            print(f"Total Amount Failed: {error}")
            connection.rollback()
            return    

    payment_status = ("Pending")
    
    try:
        query = """
        INSERT INTO payments (
            booking_id,
            payment_method,
            amount,
            payment_status
        ) VALUES (%s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (
            booking_id,
            payment_method,
            total,
            payment_status,  
            ),
        )
        connection.commit()

    except Exception as error:
        print(f"Create Payment failed: {error}")
        connection.rollback()
        return

    finally:
        cursor.close()  
        connection.close()  

    print("Create Payment Successful!")


def Verify_payment():

    booking_id = input("Booking id : ")

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT EXISTS(SELECT 1 FROM bookings WHERE booking_id = %s)"
    cursor.execute(query, (booking_id,))


    id_exists = cursor.fetchone()

    if not id_exists:
        print("Booking ID not exists.")
        cursor.close()
        connection.close()
        return

    try:
        query = """
            SELECT * FROM payments
        """
        cursor.execute(query)

        history = cursor.fetchall()
        
        if history:
            print("\n================ Payment History ================")

            for hstry in history:
                print("-" * 40)
                
                for column, value in hstry.items():
                    print(f"  {column.replace('_', ' ').title()}: {value}")
            print("\n===================================================")
        else:
            print("\n❌ No history found in the database.")

    except Exception as error:
        print(f"Payment history failed: {error}")
        cursor.close()
        connection.close()
        return

    verification = input("Verification ?[Success - Failed]: ").strip().lower()

    if verification == "success":
        payment_status = "Success" 
    elif verification == "failed":
        payment_status = "Failed"   
    else:
        print("Invalid choice! Please type Success or Failed.")
        return


    try:
        query = "UPDATE payments SET payment_status = %s WHERE booking_id = %s"
        cursor.execute(query, (payment_status, booking_id))

        if cursor.rowcount == 0:
            print("No matching payment found to update.")
        else:
            connection.commit()
            print("Verify payment Successful!")

    except Exception as error:
        print(f"Cancellion failed: {error}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()


def Refund():
    booking_id = input("Booking id : ")

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT EXISTS(SELECT 1 FROM bookings WHERE booking_id = %s)"
    cursor.execute(query, (booking_id,))


    id_exists = cursor.fetchone()

    if not id_exists:
        print("Booking ID not exists.")
        cursor.close()
        connection.close()
        return

    try:
        query = """
            SELECT * FROM payments
        """
        cursor.execute(query)

        history = cursor.fetchall()
        
        if history:
            print("\n================ Payment History ================")

            for hstry in history:
                print("-" * 40)
                
                for column, value in hstry.items():
                    print(f"  {column.replace('_', ' ').title()}: {value}")
            print("\n===================================================")
        else:
            print("\n❌ No history found in the database.")

    except Exception as error:
        print(f"Payment history failed: {error}")
        cursor.close()
        connection.close()
        return

    ref = input("Refund ?[Yes or No]: ").strip().lower()

    if ref == "yes":
        payment_status = "Failed" 
    elif ref == "no":
        payment_status = "Success"   
    else:
        print("Invalid choice! Please type Yes or NO.")
        return


    try:
        query = "UPDATE payments SET payment_status = %s WHERE booking_id = %s"
        cursor.execute(query, (payment_status, booking_id))

        if cursor.rowcount == 0:
            print("No matching payment found to update.")
        else:
            connection.commit()
            print("Refund payment Successful!")

    except Exception as error:
        print(f"Cancellion failed: {error}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()



def Payments_menu():
    while True:
        print("\n1. Create Payment")
        print("2. Verify Payment")
        print("3. Refund")
        print("4. Exit")


        choice = input("Choose: ")

        valid, message = validate_menu_choice(choice)
        if not valid:
            print(message)
            return

        if choice == "1":
            Create_payment()
        elif choice == "2":
            Verify_payment()
        elif choice == "3":
            Refund()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

Payments_menu()





