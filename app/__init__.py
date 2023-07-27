from flask import Flask
from config import Config
from .models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database with the Flask app
    db.init_app(app)

    # Import and register the blueprint from views.py
    from .views import cocktail_bp

    app.register_blueprint(cocktail_bp)

    with app.app_context():
        # Create the database tables if they do not exist
        db.create_all()

    return app
