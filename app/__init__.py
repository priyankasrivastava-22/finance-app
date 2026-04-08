# This file creates the Flask application and connects all components

from flask import Flask
from .database import db
from .finance.routes import finance   # import finance blueprint

def create_app():
    app = Flask(__name__)

    # SQLite database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialize database
    db.init_app(app)

    # register finance module
    app.register_blueprint(finance)

    # create tables if not exist
    with app.app_context():
        db.create_all()

    return app