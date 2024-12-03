import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your username
        password="your_password",
        database="freelancer_marketplace"
    )
    print("Database connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
