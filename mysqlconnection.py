import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Khushi@123",
    port=3306,
    database="new_schema"
)

mycursor = conn.cursor()

conn.commit()
conn.close()

print("Connection established successfully")
