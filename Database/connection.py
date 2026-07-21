import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="5448",
        database="airline_db"
    )

print("Connected successfully!")



