import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
  host="",
  port="",
  password="" # Change this to your MySQL password
)

# Create a database if it doesn't exist
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS sqldb")

# Connect to the created database
mydb = mysql.connector.connect(
  host="",
  port="",
  password="", # Change this to your MySQL password
  database=""
)
mycursor = mydb.cursor()

# Create a table if it doesn't exist
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Insert data into the table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit() # Commit the transaction

print(mycursor.rowcount, "record inserted.")
