from app.database.database import get_connection
import bcrypt

# def authenticate(mail, password):
#     db = get_connection()
#     cursor = db.cursor()

#     try:
#         # Check if the client exists with the provided email
#         cursor.execute("SELECT password FROM client WHERE mail = %s", (mail,))
#         result = cursor.fetchone()

#         # Validate password
#         if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
#             return "Authentication successful!"
#         return "Invalid email or password."

#     finally:
#         cursor.close()
#         db.close()


def authenticate(mail, password):
    conn = get_connection()
    cursor = conn.cursor()
    
    # Récupérez l'utilisateur par email
    cursor.execute("SELECT password FROM client WHERE mail = %s", (mail,))
    result = cursor.fetchone()
    
    if result:
        # Vérifiez le mot de passe
        stored_password = result[0].encode('utf-8')  # Récupérez le mot de passe haché
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            return "Authentification réussie !"
        else:
            return "Mot de passe incorrect."
    
    return "Utilisateur non trouvé."
