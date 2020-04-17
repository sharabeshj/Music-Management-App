from flask import Flask
from flask import request, render_template,redirect,url_for
from  flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, AUDIO, configure_uploads
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from celery import Celery
from celery.utils.log import get_logger
import boto3
import os

from boto3.s3.transfer import S3Transfer

credentials = { 
    'aws_access_key_id': os.environ['AWS_CLIENT_ID'],
    'aws_secret_access_key': os.environ['AWS_CLIENT_SECRET']
}

client = boto3.client('s3', 'ap-south-1', **credentials)
transfer = S3Transfer(client)

#app config
app = Flask(__name__,template_folder="templates",static_url_path='/static')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)

#configure database
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app) 
login_manager.login_message = "You must be logged in to view this page."
login_manager.login_view = "auth.login"

#configure uploads
music = UploadSet('music',AUDIO)
configure_uploads(app,music)

# Celery configuration
app.config['CELERY_BROKER_URL'] = os.environ['CELERY_BROKER_URL']
app.config['CELERY_RESULT_BACKEND'] = os.environ['CELERY_BROKER_BACKEND']

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
logger = get_logger(__name__)

#register blueprints
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .home import home as home_blueprint
app.register_blueprint(home_blueprint)

from app import models


@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', title='Forbidden'), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title='Page Not Found'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html', title='Server Error'), 500