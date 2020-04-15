import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    CSRF_ENABLED=True
    SECRET_KEY="This is secret"
    SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']