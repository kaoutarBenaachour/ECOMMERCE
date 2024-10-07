from ..database.database import get_connection
from ..model.produit import Produit  # Import the Produit class
import mysql.connector  # Import mysql.connector for error handling

class ProductService:
    def modify_product(self, produit: Produit):
        print("Attempting to modify the product...")  # Debugging statement
        connection = get_connection()
        cursor = connection.cursor()

        try:
            # Prepare the SQL query to update the product
            sql_query = """
            UPDATE produit 
            SET nom = %s, quantite = %s, description = %s, prix = %s 
            WHERE id = %s
            """
            # Execute the query with the new product details
            cursor.execute(sql_query, (produit.nom, produit.quantite, produit.description, produit.prix, produit.id))
            connection.commit()  # Commit the changes to the database
            
            print(f"Executed query for product ID {produit.id}.")  # Debugging statement
            
            # Check if any rows were affected
            if cursor.rowcount == 0:
                print(f"Product with ID {produit.id} not found.")
            else:
                print(f"Product with ID {produit.id} has been updated successfully.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            cursor.close()  # Close the cursor
            connection.close()  # Close the connection
