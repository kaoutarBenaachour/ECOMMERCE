from flask import Blueprint, render_template, jsonify
from app.service.deleteproduct import deleteproduct  # Corrected path to deleteproduct function
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

# Route for deleting a product
@main.route('/delete_product/<int:id>', methods=['DELETE'])
def delete_product_route(id):
    result = deleteproduct(id)  # Call the deleteproduct function with the product ID
    return jsonify({"message": result})  # Return the result as a JSON response