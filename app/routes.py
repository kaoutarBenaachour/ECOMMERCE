import bcrypt
from flask import Blueprint, app, jsonify, render_template, request
from app.database.database import get_connection
from app.service.deleteproduct import deleteproduct  # Corrected path to deleteproduct function
main = Blueprint('main', __name__) 
from app.service.addProduct import add_product  # Corrected path to addproduct function


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

# Route for deleting a product
@main.route('/delete_product/<int:id>', methods=['DELETE'])
def delete_product_route(id):
    result = deleteproduct(id)  # Call the deleteproduct function with the product ID
    return jsonify({"message": result})  # Return the result as a JSON response

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

# Route for adding a product
@main.route('/add_product/<int:id>', methods=['ADD'])
def add_product_route(id):
    result = add_product(id) 
    return jsonify({"message": result})  