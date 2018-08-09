from .. import db


class FileGithub(db.Model):
    __tablename__ = 'filegithub'
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(256))
    file_md5 = db.Column(db.String(128))

    def __repr__(self):
        return '%s %s %s' % (self.id, self.file_name, self.file_md5)
