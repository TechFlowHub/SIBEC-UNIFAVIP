from .connection import get_connection

def create_users_table():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        password_hash VARCHAR(255) NOT NULL,
        role ENUM('admin', 'secretary', 'coordinator') NOT NULL
    )
    """
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()

    cursor.close()
    conn.close()
    return users

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()
    return user

def create_user(name, email, password_hash, role):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO users (name, email, password_hash, role) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, email, password_hash, role))

    conn.commit()
    cursor.close()
    conn.close()
    return cursor.lastrowid

if __name__ == "__main__":
    for user in get_all_users():
        print(user)