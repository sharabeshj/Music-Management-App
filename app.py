from flask import Flask
from flask import request, render_template,redirect,url_for
from  flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, AUDIO, configure_uploads

import os

#app config
app = Flask(__name__,template_folder="templates")
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#configure database
db = SQLAlchemy(app)

#configure uploads
music = UploadSet('music',AUDIO)
configure_uploads(app,music)

#import models
@app.route("/")
def hello():
    return "hello world"

@app.route("/create", methods=['GET','POST'])
def create_music():
    if request.method =='POST' and 'music' in request.files:
        try:
            filename = music.save(request.files['music'])
            url = music.url(filename)
            new_music = Music(request.form['title'],request.form['album'],request.form['artist'],url)
            db.session.add(new_music)
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect(url_for('read_music'))
    else:
        return render_template('add_music.html')

if __name__=="__main__":
    app.run()