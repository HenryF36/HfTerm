import sqlite3
import os
import hashlib

# Connect to SQLite database (creates file if it doesn't exist)
connection = sqlite3.connect("HFterm.db")

cursor = connection.cursor()  # Create a cursor object

# Create the users table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, 
    name TEXT UNIQUE, 
    password TEXT
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
WHERE name = ?;
"""
cursor.execute(query, (사용자,))

# Fetch the result
user_data = cursor.fetchone()

if user_data:
    print(f"User '{사용자}' exists.")
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
        insert_query = "INSERT INTO users (name, password) VALUES (?, ?)"
        cursor.execute(insert_query, (사용자, hashed_password))
        print(f"User '{사용자}' has been created.")
        Good = True
    else:
        print("Passwords do not match. User was not created.")
        Good = False

if Good:
    os.system('cls' if os.name == 'nt' else 'clear')
    connection.commit()
    print(f"HfTerm (c) 2024 under the Apache License 2.0 ")
    print(f"Currently Running at {os.getcwd()}")
    print("")

    # Command loop
    while True:
        com = input(f"{사용자}@{os.getcwd()}> ")

# Commit changes and close the connection
connection.close()