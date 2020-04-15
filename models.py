from app import db

class Music(db.Model):
    __tablename__ = "musics"

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    album = db.Column(db.String())
    artist = db.Column(db.String())
    upload_type = db.Column(db.String(),default = "local")
    url = db.Column(db.String())

    def __init__(self, title, album, artist):
        self.title = title
        self.album = album
        self.artist = artist

    def __repr__(self):
        return "{}".format(self.url)


