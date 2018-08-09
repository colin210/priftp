from config import ALLOWED_EXTENSIONS
import hashlib


#判断后缀
def allowd_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def make_md5(file):
    md5 = hashlib.md5()
    md5.update(file)
    return md5.hexdigest()

