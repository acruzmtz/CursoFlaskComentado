from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
boostrap = Bootstrap(app)

app.config["SECRET_KEY"] = "mi llave secreta"

todos = ['Mandar diseños navidad', 'Cerrar trato con proveedor', 'Entregar avances Break Food']

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario: ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirma Password', validators=[DataRequired()])

    if password == confirm_password:
        print('son iguales')
    else:
        print('no lo son')

    submit = SubmitField('Enviar')


@app.route('/')
def home():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    login = LoginForm()
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login': login,
        'username': username
    }

    if login.validate_on_submit():
        username = login.username.data
        session['username'] = username

        flash('Usuario registrado con exito')
        return redirect(url_for('home'))


    #raise(Exception('500 Error'))
    return render_template('hello.html', **context)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error= error)




if __name__ == '__main__':
    app.run(debug=True)
