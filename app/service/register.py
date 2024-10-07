from app.model.Client import Client
from app.database.database import get_connection
import bcrypt

# def register(id, nom, prenom, mail, password, numTele):
#     db = get_connection()
#     cursor = db.cursor()

#     try:
#         # Check if the email already exists
#         cursor.execute("SELECT * FROM client WHERE mail = %s", (mail,))
#         if cursor.fetchone():
#             return "Client with this email already exists."

#         # Hash the password
#         hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#         # Insert the new client into the database
#         cursor.execute(
#             "INSERT INTO client (id, nom, prenom, mail, numTele, password) VALUES (%s, %s, %s, %s, %s, %s)",
#             (id, nom, prenom, mail, hashed_password.decode('utf-8'), numTele)
#         )
#         db.commit()
#         return "Client registered successfully!"

#     finally:
#         cursor.close()
#         db.close()


import bcrypt

def register(id, nom, prenom, mail, password, numTele):
    conn = get_connection()
    cursor = conn.cursor()
    
    # Vérifiez d'abord si l'utilisateur existe déjà
    cursor.execute("SELECT * FROM client WHERE mail = %s", (mail,))
    result = cursor.fetchone()
    
    if result:
        return "Cet email est déjà enregistré."
    
    # Hashage du mot de passe
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insérez le nouvel utilisateur dans la table client
    cursor.execute("INSERT INTO client (id, nom, prenom, mail, password, numTele) VALUES (%s, %s, %s, %s, %s, %s)",
                   (id, nom, prenom, mail, hashed_password.decode('utf-8'), numTele))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return "Inscription réussie !"
