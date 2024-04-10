import mysql.connector
import config as con
connection = mysql.connector.connect(
    user=con.MYSQL_DATABASE_USER,
    password=con.MYSQL_DATABASE_PASSWORD,
    host=con.MYSQL_DATABASE_HOST,
    database=con.MYSQL_DATABASE_DB
)
