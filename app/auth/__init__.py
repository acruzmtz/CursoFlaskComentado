from flask import Blueprint

#Recibe nombre del Blueprint, nombre de archivo, prefijo para enrutar
auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import views
