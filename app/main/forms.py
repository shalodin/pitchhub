from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchesForm(FlaskForm):

    pitch_title = StringField('Title',validators=[Required()])
    pitch_category = SelectField('Category',choices=[('Select category',
                                           'Select category'),
                                          ('sports', 'sports'),
                                          ('interview','interview'),
                                          ('business','Business'),
                                          ('love', 'love'),
                                          ('politics','Politics'),
                                          ('study','study')], validators=[Required()])
    pitch_comment = TextAreaField('New Pitch')
    submit = SubmitField('Submit')


class CategoryForm(FlaskForm):
    """
    classify a pitch
    """
    name = StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')


class CommentForm(FlaskForm):
    """
        form for creating a pitch comment
    """
    opinion = TextAreaField('COMMENT ON PITCH')
    submit = SubmitField('SUBMIT')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')