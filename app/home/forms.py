from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField


class MusicForm(FlaskForm):
    """
    Form for users to create new account
    """
    title = StringField('Title')
    artist = StringField('Artist')
    album = StringField('Album')
    music = FileField("Music")
    submit = SubmitField('Add')