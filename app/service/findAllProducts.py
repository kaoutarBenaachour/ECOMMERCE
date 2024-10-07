def get_all_produits():
    # Obtenir la connexion à la base de données
    connection = get_connection()
    cursor = connection.cursor()

    # Exécuter la requête pour obtenir tous les produits
    cursor.execute("SELECT id, nom, quantite, description, prix FROM produit")
    rows = cursor.fetchall()

    # Fermer le curseur et la connexion
    cursor.close()
    connection.close()

    # Créer une liste de produits à partir des résultats
    produits = [Produit(row[0], row[1], row[2], row[3], row[4]) for row in rows]
    return produits

# Exemple d'utilisation
produits = get_all_produits()
for produit in produits:
    print(produit.to_dict())
