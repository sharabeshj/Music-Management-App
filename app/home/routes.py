from app import music,db,celery,logger,app,client,transfer
from app.models import Music
from flask_login import login_required,current_user
import os


from . import home
from .forms import MusicForm

from flask import request,render_template,redirect,url_for

@home.route("/",methods=['GET'])
def homepage():
    return render_template('home/index.html',title="Welcome")

@celery.task
def s3_upload(id,filename):
    try:
        music = Music.query.get_or_404(id)
        transfer.upload_file(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/static/music/' + filename, 'flask-public-store', str(music.id) + '/'+ music.title+'/'+filename,
                     extra_args={'ACL': 'public-read'})
        file_url = '%s/%s/%s' % (client.meta.endpoint_url, 'flask-public-store', str(music.id) + '/'+ music.title+'/'+filename)
        music.url = file_url
        with app.app_context():
            res = render_template('s3/index.html',song = music)
            logger.info(res)
            f = open(os.path.dirname(os.path.abspath(__file__)) + "/index.html","w")
            f.write(res)
            f.close()
            transfer.upload_file(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/static/css/style.css', 'flask-public-store', str(music.id) + '/'+ music.title+'/index.css',
                     extra_args={'ACL': 'public-read'})
            transfer.upload_file(os.path.dirname(os.path.abspath(__file__)) + '/index.html', 'flask-public-store', str(music.id) + '/'+ music.title+'/'+"index.html",
                     extra_args={'ACL': 'public-read'})
            file_url = '%s/%s/%s' % (client.meta.endpoint_url, 'flask-public-store', str(music.id) + '/'+ music.title+'/index.html')
            music.s3_url = file_url
            music.s3_upload = True
            db.session.commit()
        os.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/static/music/' + filename)
    except Exception as e:
        logger.exception(e)

@home.route("/create", methods=['GET','POST'])
@login_required
def create_music():

    form = MusicForm()
    

    if form.is_submitted():
        
        try:
            filename = music.save(request.files['music'])
            url = music.url(filename)
            new_music = Music(request.form['title'],request.form['album'],request.form['artist'],url)
            new_music.user_id = current_user.get_id()
            db.session.add(new_music)
            db.session.commit()
            try:
                task = s3_upload.apply_async([new_music.id,filename])
            except Exception as e:
                print(e)
            return redirect(url_for('home.list_music'))
        except Exception as e:
            print(e)
    return render_template('home/add_music.html',form=form,title="Add Music")

@home.route("/list",methods=['GET'])
@login_required
def list_music():
    music = Music.query.filter_by(user_id = current_user.get_id()).all()
    return render_template('home/list_music.html',music = music)

@home.route('/music/<int:id>',methods=['GET','POST'])
def get_music(id):
    music = Music.query.get_or_404(id)
    print(music.s3_upload)
    return render_template('home/show_music.html',song = music)

@home.route("/delete/<int:id>",methods=['GET'])
def delete_music(id):
    music = Music.query.get_or_404(id)
    objects_to_delete = client.list_objects(Bucket="flask-public-store", Prefix="{}/{}/".format(music.id,music.title))

    delete_keys = {'Objects' : []}
    delete_keys['Objects'] = [{'Key' : k} for k in [obj['Key'] for obj in objects_to_delete.get('Contents', [])]]

    client.delete_objects(Bucket="flask-public-store", Delete=delete_keys)
    db.session.delete(music)
    db.session.commit()
    return redirect(url_for('home.list_music'))