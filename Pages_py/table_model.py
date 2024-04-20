import mysql.connector
import config as con
connection = mysql.connector.connect(
    user=con.MYSQL_DATABASE_USER,
    password=con.MYSQL_DATABASE_PASSWORD,
    host=con.MYSQL_DATABASE_HOST,
    database=con.MYSQL_DATABASE_DB
)

cursor= connection.cursor()

cursor.execute("SELECT * FROM user")
data=cursor.fetchall()
for x in data:
  print(x)

