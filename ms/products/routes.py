from ms.products import products_blueprint
from flask import request, make_response, jsonify, abort
from ms.validations.product import ProductValidation
from ms.models.product import Product
from ms import db
import json
import os

@products_blueprint.route('/', methods=['GET'])
def index():
    response_object = {
        'status': 'success',
        'container_id': os.uname()[1]
    }
    
    response_object['products'] = [product.to_json() for product in Product.query.all()]
    return make_response(jsonify(response_object), 200)


@products_blueprint.route('/', methods=['POST'])
def create():
    response_object = {
        'status': 'success',
        'container_id': os.uname()[1]
    }
    
    request_data = request.get_json()
    val = json.loads(ProductValidation.create_update_request(request_data))
    if val['invalid']:
        abort(400, description=json.dumps(val['data']))

    name = request_data['name']
    uom = request_data['uom']
    quantity = request_data['quantity']
    price = request_data['price']
    in_stock = request_data['in_stock']
    try:
        product = Product(name=name, uom=uom, quantity=quantity, price=price, in_stock=in_stock)
        db.session.add(product)
        db.session.commit()
    except Exception as e:
        abort(400, description=e)

    response_object['message'] = 'Product Added'
    response_object['product'] = Product.to_json(product)
    return make_response(jsonify(response_object), 201)


@products_blueprint.route('/<product_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def single_product(product_id):
    response_object = {
      'status': 'success',
      'container_id': os.uname()[1]
    }

    product = Product.query.filter_by(id=product_id).first()
    if product is None:
        abort(404, description='Product not found')


    if request.method == 'GET':
        response_object['product'] = Product.to_json(product)
        return make_response(jsonify(response_object), 200)
    

    if request.method == 'PUT' or request.method == 'PATCH':
        request_data = request.get_json()
        val = json.loads(ProductValidation.create_update_request(request_data))
        if val['invalid']:
            abort(400, description=json.dumps(val['data']))

        product.name = request_data['name']
        product.uom = request_data['uom']
        product.quantity = request_data['quantity']
        product.price = request_data['price']
        product.in_stock = request_data['in_stock']
        try:
            db.session.commit()
        except Exception as e:
            abort(400, description=e)

        response_object['message'] = 'Product Updated'
        response_object['product'] = Product.to_json(product)
        return make_response(jsonify(response_object), 200)


    if request.method == 'DELETE':
        db.session.delete(product)
        db.session.commit()
        response_object['message'] = 'Product Deleted'
        return make_response(jsonify(response_object), 204)

