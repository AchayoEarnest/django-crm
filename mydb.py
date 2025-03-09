import mysql.connector

# Establish the database connection
database = mysql.connector.connect(
    host='localhost',
    user='earnest',
    passwd='access2023'
)

# Prepare a cursor object
cursorObject = database.cursor()

# Execute the SQL query to create the database
cursorObject.execute('CREATE DATABASE elderco')

print("All Done!")
