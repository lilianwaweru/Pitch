from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators=[Required()])
    submit = SubmitField('Submit')
    

class PitchForm(FlaskForm):
    pitch = TextAreaField('pitch',validators=[Required()])
    category = SelectField('Category',choices=[('interview','interview'),('pickup lines','pickup lines'),('product','product'),('promotion','promotion')],validators=[Required()]) 
    submit = SubmitField('submit')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('write your comment',validators=[Required()])
    submit = SubmitField('submit')

