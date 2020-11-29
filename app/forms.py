from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    # confirm_password = PasswordField('Confirma Password', validators=[DataRequired()])
    #
    # if password == confirm_password:
    #     print('son iguales')
    # else:
    #     print('no lo son')

    submit = SubmitField('send')


class TodoForm(FlaskForm):
    #name = StringField('Task: ', validators=[DataRequired()])
    description = StringField('Description: ', validators=[DataRequired()])
    submit = SubmitField('Save')

class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Delete')

class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Update')

