import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate


# Instantiate SQLAlchemy Extension
db = SQLAlchemy()
migrate = Migrate()


def create_app(script_info=None):

    # Instantiate App
    app = Flask(__name__)

    # Enable CORS
    CORS(app)

    # Set Config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # Initialize Flask Extensions
    db.init_app(app)
    migrate.init_app(app, db)


    # Register Blueprints
    from ms.customers import customers_blueprint
    app.register_blueprint(customers_blueprint, url_prefix='/api/v1/customers')

    from ms.products import products_blueprint
    app.register_blueprint(products_blueprint, url_prefix='/api/v1/products')


    # Default Route
    @app.route('/api/v1/health', methods=['GET'])
    def status():
        return jsonify({
            'status': 'success',
            'message': 'server up!',
            'container_id': os.uname()[1]
        })

    @app.route('/api/v1/hotreload', methods=['GET'])
    def reload():
        return jsonify({
            'status': 'success',
            'message': 'Test Hot Reload by changing this message!',
            'container_id': os.uname()[1]
        })


    # Error Handling
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error=str(e)), 400

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify(error=str(e)), 500


    # Shell Context for Flask CLI
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}


    return app