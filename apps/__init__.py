from flask import Flask, session
from flask_session import Session
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
import os
import logging


from apps.database.db import initialize_db

from importlib import import_module

#from apps.database.models import Users

db = initialize_db()
login_manager = LoginManager()

# Logging Setup
logger = logging.getLogger('werkzeug')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(os.path.join(os.getcwd(),"log","biodiversity_api.log"), 'a+', 'utf-8')
formatter = logging.Formatter('%(asctime)s %(levelname)s : %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
handler.setFormatter(formatter) # Pass handler as a parameter, not assign
logger.addHandler(handler)
logger.warning('[INFO] Start Logging...')


def register_extensions(app):
    #db.init_app(app)
    login_manager.init_app(app)
    print("[INFO] Extension Registered")

def register_blueprints(app):
    login_module = import_module('apps.{}.routes'.format("login"))
    logout_module = import_module('apps.{}.routes'.format("logout"))
    admin_module = import_module('apps.{}.routes'.format("admin"))
    user_module = import_module('apps.{}.routes'.format("user"))

    app.register_blueprint(login_module.login_bp)
    app.register_blueprint(logout_module.logout_bp)
    app.register_blueprint(admin_module.admin_bp)
    app.register_blueprint(user_module.user_bp)

    print("[INFO] Blueprint Registered")

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    Session(app)
    register_extensions(app)
    register_blueprints(app)
    return app
