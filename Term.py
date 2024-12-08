import mysql.connector
import os
import hashlib
from Commands import Comm

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="HFterm",    # Replace with your MySQL username
  password="HFHF",  # Replace with your MySQL password
  database="HFterm"         # The database you created earlier
)

cursor = mydb.cursor()  # Create a cursor object
# Create the users table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(255) UNIQUE, 
    password VARCHAR(255)
)
""")
print("Welcome to SQLstore Python!")

# Get username input and standardize it
사용자 = input("Enter username: ").strip()
사용자 = 사용자.lower().capitalize()

# Query to check if the user exists
query = """
SELECT password 
FROM users 
WHERE name = %s;
"""
cursor.execute(query, (사용자,))

# Fetch the result
user_data = cursor.fetchone() # Fetch One

if user_data:
    passEntered = input("Enter Password: ").strip()
    
    # Compare hashed passwords
    stored_password = user_data[0]
    hashed_entered_password = hashlib.sha256(passEntered.encode()).hexdigest()

    if hashed_entered_password == stored_password:
        print("Password is correct.")
        Good = True
    else:
        print("Incorrect password.")
        Good = False
else:
    print(f"User '{사용자}' does not exist.")
    p1 = input("Enter a new password: ").strip()
    p2 = input("Enter the same password: ").strip()
    
    if p1 == p2:
        print("Passwords are valid.")
        # Hash the password for storage (use hashlib for security)
        hashed_password = hashlib.sha256(p1.encode()).hexdigest()
        
        # Insert the new user into the database
        insert_query = "INSERT INTO users (name, password) VALUES (%s, %s)"
        cursor.execute(insert_query, (사용자, hashed_password))
        print(f"User '{사용자}' has been created.")
        Good = True
    else:
        print("Passwords do not match. User was not created.")
        Good = False

if Good:
    os.system('cls' if os.name == 'nt' else 'clear')
    mydb.commit()  # Commit changes to the MySQL database
    print(f"HfTerm (c) 2024 under the Apache License 2.0 ")
    print(f"Currently Running at {os.getcwd()}")
    print("")

    # Command loop
    while True:
        com = input(f"{사용자}@{os.getcwd()}> ")
        Comm(사용자, com, os.getcwd())

# Commit changes and close the connection
mydb.close()
