from flask import Flask
from flask import request, render_template,redirect,url_for
from  flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, AUDIO, configure_uploads
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

import os

#app config
app = Flask(__name__,template_folder="templates",static_url_path='/static')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)

#configure database
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_message = "You must be logged in to view this page."
login_manager.login_view = "auth.login"

#configure uploads
music = UploadSet('music',AUDIO)
configure_uploads(app,music)

#register blueprints
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .home import home as home_blueprint
app.register_blueprint(home_blueprint)

from app import models