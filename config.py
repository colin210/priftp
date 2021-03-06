import os
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = 'upload'


class Config:
    SECRET_KEY = 'priftp'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    Debug = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:lin85210@localhost:3306/priftp'
    UPLOAD_FOLDER = '/upload/'
    SQLALCHEMY_TRACK_MODIFICATIONS = True



class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}

ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg',
                          'xls', 'JPG', 'PNG',
                          'xlsx', 'gif', 'GIF'])