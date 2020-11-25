from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .auth import auth

def create_app():

    app = Flask(__name__)
    boostrap = Bootstrap(app)

    app.config.from_object(Config)

    #Registramos el blueprint
    app.register_blueprint(auth)

    return app
