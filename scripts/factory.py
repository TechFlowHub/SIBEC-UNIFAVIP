from database.connection import get_connection
from utils.password import hash_password

def create_admin():
    conn = get_connection()
    cursor = conn.cursor()

    email = "admin"
    password = hash_password("admin")
    role = "admin"

    query = "INSERT INTO users (email, password_hash, role) VALUES (%s, %s, %s)"
    cursor.execute(query, (email, password, role))
    conn.commit()

    cursor.close()
    conn.close()
    print("Admin criado com sucesso!")

def create_secretary():
    conn = get_connection()
    cursor = conn.cursor()

    email = "secretary"
    password = hash_password("123")
    role = "secretary"

    query = "INSERT INTO users (email, password_hash, role) VALUES (%s, %s, %s)"
    cursor.execute(query, (email, password, role))
    conn.commit()

    cursor.close()
    conn.close()
    print("Secretario criado com sucesso!")
