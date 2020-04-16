import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    CSRF_ENABLED=True
    SECRET_KEY="This is secret"
    SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
    # Uploads
    UPLOADS_DEFAULT_DEST = basedir + '/app/static/'
    UPLOADS_DEFAULT_URL = '{}/static/'.format(os.environ['HOST_NAME'])
    
    UPLOADED_AUDIO_DEST = basedir + '/project/static/'
    UPLOADED_AUDIO_URL = '{}/static/'.format(os.environ['HOST_NAME'])
