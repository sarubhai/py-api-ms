from flask import Blueprint

customers_blueprint = Blueprint('customers', __name__)

from ms.customers import routes