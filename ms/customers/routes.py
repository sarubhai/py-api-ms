from ms.customers import customers_blueprint
from flask import request, make_response, jsonify, abort
from ms.validations.customer import CustomerValidation
from ms.models.customer import Customer
import json

@customers_blueprint.route('/', methods=['GET'])
def index():
    return make_response(jsonify({'customers': Customer.get_all_customers()}), 200)


@customers_blueprint.route('/', methods=['POST'])
def create():
    request_data = request.get_json()
    val = json.loads(CustomerValidation.create_update_request(request_data))
    if val['invalid']:
        abort(400, description=json.dumps(val['data']))
    
    try:
        customer = Customer.add_customer(request_data['name'], request_data['dob'], request_data['address'])
    except Exception as e:
        abort(400, description=e)
    
    return make_response(jsonify(customer), 201)


@customers_blueprint.route('/<int:id>', methods=['GET'])
def show(id):
    customer = Customer.get_customer_by_id(id)
    if customer is None:
        abort(404, description="Customer not found")

    return make_response(jsonify(customer), 200)


@customers_blueprint.route('/<int:id>', methods=['PUT','PATCH'])
def update(id):
    request_data = request.get_json()
    val = json.loads(CustomerValidation.create_update_request(request_data))
    if val['invalid']:
        abort(400, description=json.dumps(val['data']))
    
    try:
        customer = Customer.update_customer(id, request_data['name'], request_data['dob'], request_data['address'])
    except Exception as e:
        abort(400, description=e)
    
    if customer is None:
        abort(404, description="Customer not found")
    
    return make_response(jsonify(customer), 200)


@customers_blueprint.route('/<int:id>', methods=['DELETE'])
def destroy(id):
    Customer.delete_customer(id)
    return make_response(jsonify({}), 204)
