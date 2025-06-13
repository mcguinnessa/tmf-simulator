from flask import Blueprint, jsonify, current_app

tmf637_bp = Blueprint('tmf637_bp', __name__)
from tmf637_data import product_inventory

#
# TMF637 Product Inventory
#
# GET /product/{id}?fields=
# DELETE /product/{id}
# GET /product?fields=
# PATCH /product/{id}?fields=
# POST /product?fields=
# POST /hub
# DELETE /hub/{id}
# POST /client/listener



@tmf637_bp.route('/product', methods=['GET'])
def get_products():
    return jsonify(product_inventory)

@tmf637_bp.route('/product/<string:id>', methods=['GET'])
def get_product(id):
   spec = product_inventory.get(id)
   if spec:
      return jsonify(spec)
   return jsonify({"error": "Product not found"}), 404




