from app.database.database import get_connection

def add_product(nom, quantite, description, prix):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO produit (nom, quantite, description, prix)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (nom, quantite, description, prix))
        connection.commit()
        return cursor.lastrowid  # Return the ID of the newly created product
    except Exception as e:
        print(f"Error adding product: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()