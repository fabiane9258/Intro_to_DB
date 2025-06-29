import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (adjust host/user/password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Sierra!9258'  # ← replace with your real password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close cursor and connection safely
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
