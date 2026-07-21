import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="5448",
        database="airline_db"
    )

    return connection


