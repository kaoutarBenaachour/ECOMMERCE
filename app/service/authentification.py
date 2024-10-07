from database.database import get_connection

def authenticate(mail, password):
    db = get_connection()
    cursor = db.cursor()

    try:
        # Check if the client exists with the provided email and password
        cursor.execute("SELECT * FROM clients WHERE mail = %s AND password = %s", (mail, password))
        if cursor.fetchone():
            return "Authentication successful!"
        return "Invalid email or password."
    
    finally:
        cursor.close()
        db.close()
