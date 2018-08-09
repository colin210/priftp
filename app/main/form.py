from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import  FileField,FileAllowed, FileRequired
from flask_uploads import UploadSet, IMAGES

images = UploadSet('images', IMAGES)


class FileForm(FlaskForm):
    filename = FileField('img', validators=[FileRequired(),
                                        FileAllowed(images, 'image only')])
    submit = SubmitField('Add')
