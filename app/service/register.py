from client import Client
from database.database import get_connection

def register(id, nom, prenom, mail, password, numTele):
    db = get_connection()
    cursor = db.cursor()

    try:
        # Check if the email already exists
        cursor.execute("SELECT * FROM clients WHERE mail = %s", (mail,))
        if cursor.fetchone():
            return "Client with this email already exists."

        # Insert the new client into the database
        cursor.execute(
            "INSERT INTO clients (id, nom, prenom, mail, password, numTele) VALUES (%s, %s, %s, %s, %s, %s)",
            (id, nom, prenom, mail, password, numTele)
        )
        db.commit()
        return "Client registered successfully!"
    
    finally:
        cursor.close()
        db.close()
