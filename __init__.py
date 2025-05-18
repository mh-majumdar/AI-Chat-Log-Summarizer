from flask import Flask
from flask_login import LoginManager
from .extensions import db

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

   

    # Register blueprints
   

   


    # Create database
    with app.app_context():
        db.create_all()
        print("Database created!")

    return app