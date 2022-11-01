from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(testing = None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    if testing is None:
        app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config['TESTING'] =True
        app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')
   
    # DB Config
    db.init_app(app)
    migrate.init_app(app, db)
    load_dotenv()

    #register model
    from app.models.breakfast import Breakfast
    from .routes.breakfast import breakfast_bp
    app.register_blueprint(breakfast_bp)
    
    return app