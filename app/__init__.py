from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .config import Config
from .auth import auth
from .models import UserLogin

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(username):
    return UserLogin.query(username)

def create_app():

    app = Flask(__name__)
    boostrap = Bootstrap(app)

    app.config.from_object(Config)

    #iniciamos login manager
    login_manager.init_app(app)

    #Registramos el blueprint
    app.register_blueprint(auth)

    return app
