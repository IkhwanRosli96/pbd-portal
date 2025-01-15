from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, HiddenField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, EqualTo, InputRequired

class CreateUserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    privilege = SelectField('Privilege', choices=[(0, 'Super Admin'), (1, 'Admin'), (2, 'User')])
    allowed_collections = SelectMultipleField('Allowed Collections', coerce=str)
    submit = SubmitField('Create User')

class UpdatePasswordForm(FlaskForm):
    username = HiddenField('Username', validators=[InputRequired()])
    current_pwd = PasswordField('Your Password', validators=[InputRequired()])
    new_pwd = PasswordField('New Password for Selected User', validators=[InputRequired(), EqualTo('confirm_pwd', message='Passwords must match')])
    confirm_pwd = PasswordField('Re-input New Password for Selected User', validators=[InputRequired()])
    submit = SubmitField('Update Password')

class UpdateUserForm(FlaskForm):
    selected_user = HiddenField('Selected User', validators=[InputRequired()])
    username = StringField('Username', validators=[])
    current_privilege = StringField('Current Privilege', validators=[])
    current_allowed_collection = StringField('Current Allowed Collection', validators=[])
    new_allowed_collections = SelectMultipleField('Allowed Collections', coerce=str)
    submit = SubmitField('Update User')
    
class deleteUserForm(FlaskForm):
    username = HiddenField('username', validators=[InputRequired()])
    submit = SubmitField('Delete User')
