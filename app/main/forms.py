from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import TextAreaField,SubmitField,StringField
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Update bio.',validators = [Required()])
    submit = SubmitField('Update')

class PostAPitch (FlaskForm):
    title = StringField('Title',validators = [Required()])
    content = TextAreaField('Pitch',validators = [Required()])
    submit = SubmitField('Pitch')

class PostAComment (FlaskForm):
    comment = TextAreaField(validators = [Required()])
    submit = SubmitField('Comment',validators = [Required()])
