from flask import Flask,render_template,jsonify,request,redirect,url_for
from . import main
import time, os, base64
from .fun import make_md5
from werkzeug.utils import secure_filename
from config import basedir, UPLOAD_FOLDER
from .form import FileForm
from .models import FileGithub
from app import db

file_dir = os.path.join(basedir, UPLOAD_FOLDER)


@main.route('/',  methods=['GET', 'POST'], strict_slashes=False)
def index():
    form = FileForm()
    #
    if form.is_submitted():
        f = form.filename.data
        fname = secure_filename(f.filename)
        ext = fname.rsplit('.', 1)[1]
        new_filename = (fname.rsplit('.', 1)[0]) + '.' + ext

        if FileGithub.query.filter_by(file_name=new_filename).all():
            res = 'file is exist'
            print('exsit')
        else:
        #保存文件
            print('to db')
            f.save(os.path.join(file_dir, new_filename))

        #落库
            f_indb = FileGithub(file_name=new_filename, file_md5=make_md5(new_filename.encode()))
            db.session.add(f_indb)
            db.session.commit()

            res = 'upload succeed'
        return render_template('main/index.html', form=form, res=res)
    return render_template('main/index.html', form=form)


@main.route('/files', methods=['GEt', 'POST'])
def files():
    all_files = FileGithub.query.all()
    return render_template('main/files.html', files_all=all_files)


@main.route('/delfile/<id>', methods=['GET', 'POST'])
def delfile(id):
    file_del = FileGithub.query.get(id)
    rm_filename = file_dir+'/'+file_del.file_name

    if file_del:
        try:
            os.remove(rm_filename)

            db.session.delete(file_del)
            db.session.commit()

        except Exception as e:
            print(e)
            db.session.rollback()
    return redirect(url_for('main.files'))
