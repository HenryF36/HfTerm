import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="HFterm",    # Replace with your MySQL username
  password="HFHF"#,  # Replace with your MySQL password
  #database="HFterm"         # The database you created earlier
)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)