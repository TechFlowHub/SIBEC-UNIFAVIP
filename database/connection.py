import mysql.connector
from config import Config

def get_connection():
    return mysql.connector.connect(
        host = Config.DB_HOST,
        user = Config.DB_USER,
        password = Config.DB_PASSWORD,
        database = Config.DB_NAME
    )

def test_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    
if __name__ == "__main__":
    if test_connection():
        print("Database connection successful.")
    else:
        print("Database connection failed.")