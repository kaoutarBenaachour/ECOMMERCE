from app.database.database import get_connection
from app.model.produit import Produit # Assurez-vous que le chemin est correct

def get_all_produits():
    db = get_connection()  # Connexion à la base de données
    cursor = db.cursor()

    try:
        # Exécute la requête pour récupérer tous les produits
        cursor.execute("SELECT id, nom, quantite, description, prix FROM produit")
        rows = cursor.fetchall()  # Récupère toutes les lignes

        # Crée une liste de dictionnaires de produits à partir des résultats
        produits = []
        for row in rows:
            produit = Produit(row[0], row[1], row[2], row[3], row[4])
            produits.append(produit.to_dict())  # Utilisation de la méthode to_dict()

        return produits  # Retourne la liste des produits sous forme de dictionnaire

    except Exception as e:
        return f"Error occurred: {str(e)}"  # Retourne une erreur si quelque chose échoue

    finally:
        cursor.close()  # Ferme le curseur
        db.close()      # Ferme la connexion à la base de données
