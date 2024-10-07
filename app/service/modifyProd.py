from database.database import get_connection  # Import the get_connection function
from model.produit import Produit  # Import the Produit class
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

# Testing the modify_product function
if __name__ == "__main__":
    print("Starting the product modification script...")  # Debugging statement
    service = ProductService()

    # Create a Produit instance with the ID of the product you want to modify
    product_to_modify = Produit(id=3, nom="Updated Test Product", quantite=10, description="Updated description", prix=75)

    # Call the modify_product method to update the product
    service.modify_product(product_to_modify)

    # Verify changes by querying the database
    connection = get_connection()
    cursor = connection.cursor()
    
    # Fetch the updated product details
    cursor.execute("SELECT * FROM produit WHERE id = %s", (product_to_modify.id,))
    result = cursor.fetchone()

    if result:
        print("Updated Product Details:")
        print(f"ID: {result[4]}, Name: {result[0]}, Quantity: {result[1]}, Description: {result[2]}, Price: {result[3]}")
    else:
        print(f"Product with ID {product_to_modify.id} not found after update.")

    cursor.close()  # Close the cursor
    connection.close()  # Close the connection
