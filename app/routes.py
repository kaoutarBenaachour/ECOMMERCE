from flask import Blueprint, render_template, jsonify

from app.service.findAllProducts import get_all_produits  # Chemin vers la fonction pour récupérer les produits

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


# Route for listing all products
@main.route('/produits', methods=['GET'])
def liste_produits():
    produits = get_all_produits()  # Récupère tous les produits
    return render_template('index.html', produits=produits)  # Retourne le template avec la liste des produits
