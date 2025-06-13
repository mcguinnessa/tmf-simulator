from flask import Blueprint, jsonify, current_app

tmf620_bp = Blueprint('tmf620_bp', __name__)
from tmf620_data import catalogs
from tmf620_data import offerings
from tmf620_data import specifications

#
# TMF620 Product Catalogue
#
# GET /category/{id}?fields=
# PATCH /category/{id}?fields=
# GET /category?fields=
# POST /category?fields=
# DELETE /category/{id}
# GET /importJob?fields=
# POST /importJob?fields=
# GET /importJob/{id}?fields=
# DELETE /importJob/{id}
# GET /exportJob?fields=
# POST /exportJob?fields=
# GET /exportJob/{id}?fields=
# DELETE /exportJob/{id}
# GET /productCatalog/{id}?fields=
# PATCH /productCatalog/{id}?fields=
# DELETE /productCatalog/{id}
# GET /productCatalog?fields=
# POST /productCatalog?fields=
# GET /productOffering/{id}?fields=
# PATCH /productOffering/{id}?fields=
# DELETE /productOffering/{id}
# GET /productOffering?fields=
# POST /productOffering?fields=
# GET /productSpecification/{id}?fields=
# PATCH /productSpecification/{id}?fields=
# DELETE /productSpecification/{id}
# GET /productSpecification?fields=
# POST /productSpecification?fields=
# GET /productOfferingPrice/{id}?fields=
# PATCH /productOfferingPrice/{id}?fields=
# DELETE /productOfferingPrice/{id}
# GET /productOfferingPrice?fields=
# POST /productOfferingPrice?fields=
# POST /hub
# DELETE /hub
# POST /client/listener



@tmf620_bp.route('/productCatalog', methods=['GET'])
def get_product_catalogs():
#    catalogs = current_app.config['CATALOGS']
    return jsonify(catalogs)

@tmf620_bp.route('/productOffering', methods=['GET'])
def get_product_offerings():
#    catalogs = current_app.config['CATALOGS']
    return jsonify(offerings)

@tmf620_bp.route('/productSpecification/<string:id>', methods=['GET'])
def get_product_specification(id):
#    catalogs = current_app.config['CATALOGS']
#    return jsonify(catalogs)
   spec = specifications.get(id)
   if spec:
      return jsonify(spec)
   return jsonify({"error": "Product Specification not found"}), 404

#@tmf620_bp.route('/productCatalog/<string:id>', methods=['GET'])
#def get_product_catalog(id):
#   spec = product_specifications.get(spec_id)
#   if spec:
#      return jsonify(spec)
#   return jsonify({"error": "Product Specification not found"}), 404



