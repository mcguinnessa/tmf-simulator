from flask import Blueprint, jsonify, current_app

tmf620_bp = Blueprint('tmf620_bp', __name__)
from tmf620_data import catalogs
from tmf620_data import offerings
from tmf620_data import specifications
from tmf620_data import prices

#
# TMF620 Product Catalogue
#
#X GET /category/{id}?fields=
#X PATCH /category/{id}?fields=
#X GET /category?fields=
#X POST /category?fields=
#X DELETE /category/{id}
#X GET /importJob?fields=
#X POST /importJob?fields=
#X GET /importJob/{id}?fields=
#X DELETE /importJob/{id}
#X GET /exportJob?fields=
#X POST /exportJob?fields=
#X GET /exportJob/{id}?fields=
#X DELETE /exportJob/{id}
#X GET /productCatalog/{id}?fields=
#X PATCH /productCatalog/{id}?fields=
#X DELETE /productCatalog/{id}
# GET /productCatalog?fields=
#X POST /productCatalog?fields=
#X GET /productOffering/{id}?fields=
#X PATCH /productOffering/{id}?fields=
#X DELETE /productOffering/{id}
# GET /productOffering?fields=
#X POST /productOffering?fields=
# GET /productSpecification/{id}?fields=
#X PATCH /productSpecification/{id}?fields=
#X DELETE /productSpecification/{id}
#X GET /productSpecification?fields=
#X POST /productSpecification?fields=
#X GET /productOfferingPrice/{id}?fields=
#X PATCH /productOfferingPrice/{id}?fields=
# DELETE /productOfferingPrice/{id}
#X GET /productOfferingPrice?fields=
#X POST /productOfferingPrice?fields=
#X POST /hub
#X DELETE /hub
#X POST /client/listener



@tmf620_bp.route('/productCatalog', methods=['GET'])
def get_product_catalogs():
#    catalogs = current_app.config['CATALOGS']
    return jsonify(catalogs)

@tmf620_bp.route('/productOffering', methods=['GET'])
def get_product_offerings():
    return jsonify(offerings)

@tmf620_bp.route('/productOfferingPrice/<string:id>', methods=['GET'])
def get_product_offering_price():
   spec = prices.get(id)
   if spec:
      return jsonify(spec)
   return jsonify({"error": "Product Offering not found"}), 404

@tmf620_bp.route('/productSpecification/<string:id>', methods=['GET'])
def get_product_specification(id):
   spec = specifications.get(id)
   if spec:
      return jsonify(spec)
   return jsonify({"error": "Product Specification not found"}), 404



