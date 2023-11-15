import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'arafat2023'
)

cursor = database.cursor()


print('all done')