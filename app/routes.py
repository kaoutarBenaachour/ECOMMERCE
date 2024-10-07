from app.service.modifyProd import ProductService
from flask import Blueprint, render_template, jsonify

from app.service.findAllProducts import get_all_produits  # Chemin vers la fonction pour récupérer les produits
import bcrypt
from flask import Blueprint, app, jsonify, render_template, request
from app.database.database import get_connection
from app.service.deleteproduct import deleteproduct
#from produit import Produit  # Corrected path to deleteproduct function
from .model.produit import Produit  # Corrected import path
main = Blueprint('main', __name__) 
from app.service.addProduct import add_product  # Corrected path to addproduct function


from flask import Blueprint, render_template, jsonify
from app.service.deleteproduct import deleteproduct  # Corrected path to deleteproduct function
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/produits', methods=['GET'])
def liste_produits():
    produits = get_all_produits()  # Récupère tous les produits
    return jsonify(produits)  # Retourne les produits au format JSON

# Route for deleting a product
@main.route('/delete_product/<int:id>', methods=['DELETE'])
def delete_product_route(id):
    result = deleteproduct(id)  # Call the deleteproduct function with the product ID
    return jsonify({"message": result})  


# Route for modifying a product
@main.route('/modify_product', methods=['PUT'])  # Change POST to PUT if you are modifying an existing product
def modify_product():
    data = request.get_json()  # Get the JSON data from the request
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Extract product details from the request
    try:
        product_id = data['id']
        nom = data['nom']
        quantite = data['quantite']
        description = data['description']
        prix = data['prix']
    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    
    # Create an instance of Produit
    product_to_modify = Produit(id=product_id, nom=nom, quantite=quantite, description=description, prix=prix)

    # Call the modify_product method
    service = ProductService()
    service.modify_product(product_to_modify)

    return jsonify({"message": "Product updated successfully"}), 200




# Route for modifying a product
@main.route('/modify_product', methods=['PUT'])  # Change POST to PUT if you are modifying an existing product
def modify_product():
    data = request.get_json()  # Get the JSON data from the request
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Extract product details from the request
    try:
        product_id = data['id']
        nom = data['nom']
        quantite = data['quantite']
        description = data['description']
        prix = data['prix']
    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    
    # Create an instance of Produit
    product_to_modify = Produit(id=product_id, nom=nom, quantite=quantite, description=description, prix=prix)

    # Call the modify_product method
    service = ProductService()
    service.modify_product(product_to_modify)

    return jsonify({"message": "Product updated successfully"}), 200



@main.route('/register', methods=['POST'])
def register():
    data = request.json
    nom = data['nom']
    prenom = data['prenom']
    mail = data['mail']
    password = data['password']
    numTele = data['numTele']
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO client (nom, prenom, mail, password, numTele) VALUES (%s, %s, %s, %s, %s)",
                   (nom, prenom, mail, hashed_password.decode('utf-8'), numTele))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Inscription réussie!"}), 200

@main.route('/login', methods=['POST'])
def login():
    data = request.json
    mail = data['mail']
    password = data['password']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM client WHERE mail = %s", (mail,))
    result = cursor.fetchone()
    
    if result:
        stored_password = result[0].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            return jsonify({"message": "Authentification réussie!"}), 200
        else:
            return jsonify({"message": "Mot de passe incorrect!"}), 401
    return jsonify({"message": "Utilisateur non trouvé!"}), 404
    return jsonify({"message": result})  # Return the result as a JSON response

@main.route('/add_product', methods=['POST'])  # Change 'ADD' to 'POST'
def add_product_route():
    data = request.get_json()  # Get the JSON data from the request
    nom = data['nom']
    quantite = data['quantite']
    description = data['description']
    prix = data['prix']
    result = add_product(nom, quantite, description, prix)  # Pass all required parameters
    return jsonify({"message": result}) 

@main.route('/produit/<int:id>', methods=['GET'])
def get_product(id):
    print(f"Tentative de récupération du produit avec l'ID: {id}")
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM produit WHERE id = %s", (id,))
        product = cursor.fetchone()
        
        if product:
            print(f"Produit récupéré de la base de données: {product}")
            product_data = {
                'nom': product[0],
                'quantite': product[1],
                'description': product[2],
                'prix': product[3],
                'id': product[4],
            }
            print(f"Données du produit formatées pour l'envoi: {product_data}")
            return jsonify(product_data)
        else:
            print(f"Aucun produit trouvé avec l'ID: {id}")
            return jsonify({"message": "Produit non trouvé"}), 404
    except Exception as e:
        print(f"Erreur lors de la récupération du produit: {str(e)}")
        return jsonify({"message": "Erreur lors de la récupération du produit"}), 500
    finally:
        cursor.close()
        conn.close()