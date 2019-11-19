from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewUser(FlaskForm):
    """new User form."""
    username = StringField('Username', validators=[DataRequired()])
    first = StringField('First name', validators=[DataRequired()])
    last = StringField('Last name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    submit = SubmitField('Submit')
