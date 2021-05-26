from flask import Flask
#from flask_mongoalchemy import MongoAlchemy
from flask_mongoengine import MongoEngine

from .config import config_by_name
#We will be using the application factory pattern for creating our
#Flask object.
from flask_cors import CORS, cross_origin
db= MongoEngine()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    #app.config['MONGOALCHEMY_DATABASE'] = 'productinfo'
    #app.config['MONGOALCHEMY_SERVER'] = 'localhost'
    #app.config['MONGOALCHEMY_PORT'] = '27017'
    app.config['MONGODB_SETTINGS'] = {
        'db': 'productinfo',
        'host': 'localhost',
        'port': 27017
    }
    #db = MongoEngine(app)
    db.init_app(app)
    return app