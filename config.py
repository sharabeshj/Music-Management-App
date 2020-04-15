import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    CSRF_ENABLED=True
    SECRET_KEY="This is secret"
    SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
    # Uploads
    UPLOADS_DEFAULT_DEST = basedir + '/static/songs/'
    UPLOADS_DEFAULT_URL = '{}/static/songs/'.format(os.environ['HOST_NAME'])
    
    UPLOADED_AUDIO_DEST = basedir + '/project/static/songs/'
    UPLOADED_AUDIO_URL = '{}/static/songs/'.format(os.environ['HOST_NAME'])
