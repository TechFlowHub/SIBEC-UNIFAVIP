import mysql.connector
from config import Config

my_db = mysql.connector.connect(
    host = Config.DB_HOST,
    user = Config.DB_USER,
    password = Config.DB_PASSWORD,
    database = Config.DB_NAME
)

my_cursor = my_db.cursor()

if my_db.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")
