from app import db,login_manager

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
   
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Music(db.Model):
    __tablename__ = "musics"

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(60))
    album = db.Column(db.String(60))
    artist = db.Column(db.String(60))
    url = db.Column(db.String(60))
    s3_upload = db.Column(db.Boolean,default=False)
    s3_url = db.Column(db.String(60))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, album, artist,url):
        self.title = title
        self.album = album
        self.artist = artist
        self.url = url

    def __repr__(self):
        return "{}".format(self.url)


