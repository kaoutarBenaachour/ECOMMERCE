from app.database.database import get_connection

def deleteproduct(id):
    db = get_connection()
    cursor = db.cursor()

    try:
        # Check if the product exists
        cursor.execute("SELECT * FROM produit WHERE id = %s", (id,))
        product = cursor.fetchone()
        
        if product is None:
            return f"Product with id {id} does not exist."

        # Delete the product
        cursor.execute("DELETE FROM produit WHERE id = %s", (id,))
        db.commit()

        return f"Product with id {id} deleted successfully."
    
    except Exception as e:
        db.rollback()
        return f"Error occurred: {str(e)}"
    
    finally:
        cursor.close()
        db.close()
