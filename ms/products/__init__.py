from flask import Blueprint

products_blueprint = Blueprint('products', __name__)

from ms.products import routes