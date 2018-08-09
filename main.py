#encoding:utf8
from werkzeug.utils import secure_filename
import time,os,base64
from flask import Flask,render_template,jsonify,request,send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg',
                          'xls', 'JPG', 'PNG',
                          'xlsx', 'gif', 'GIF'])


#判断后缀
def allowd_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/',  methods=['GET'], strict_slashes=False)
def indexpage():
    return render_template('index.html')


@app.route('/', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config["UPLOAD_FOLDER"])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['file']

    if f and allowd_file(f.filename):
        fname = secure_filename(f.filename)
        ext = fname.rsplit('.', 1)[1]
        unix_time = int(time.time())
        new_filename = str(unix_time) +'.'+ext
        f.save(os.path.join(file_dir, new_filename))
        token = base64.b64encode(new_filename.encode())
        token = token.decode()

        return jsonify({"error": 0, "msg": "succeed", "token": token})
    else:
        return jsonify({"error": 1001, "errmsg": "fail"})


if __name__ == '__main__':
    app.run(debug=True)