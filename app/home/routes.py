from app import music,db
from app.models import Music
from flask_login import login_required

from . import home

from flask import request,render_template,redirect,url_for

@home.route("/",methods=['GET'])
def homepage():
    return render_template('home/index.html',title="Welcome")

@home.route("/create", methods=['GET','POST'])
@login_required
def create_music():
    if request.method =='POST' and 'music' in request.files:
        try:
            filename = music.save(request.files['music'])
            url = music.url(filename)
            new_music = Music(request.form['title'],request.form['album'],request.form['artist'],url)
            db.session.add(new_music)
            db.session.commit()
            return redirect(url_for('list_music'))
        except Exception as e:
            print(e)
    else:
        return render_template('add_music.html')
    return None

@home.route("/list",methods=['GET'])
@login_required
def list_music():
    music = Music.query.all()
    return render_template('list_music.html',music = music)

@home.route('/edit/<int:id>',methods=['GET','POST'])
def edit_music(id):
    music = Music.query.get_or_404(id)
    add_music = False
    if request.method == 'POST':
        music.title = request.form['title']
        music.artist = request.form['artist']
        music.album = request.form['album']
        db.session.commit()
        return redirect(url_for('list_music'))
    
    return render_template('add_music.html', add_music=add_music)

@home.route("/delete/<int:id>",methods=['GET'])
def delete_music(id):
    music = Music.query.get_or_404(id)
    db.session.delete(music)
    db.session.commit()
    return redirect(url_for('list_music'))