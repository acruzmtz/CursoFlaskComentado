from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest
from flask_login import login_required, current_user
from app import create_app
from app.forms import LoginForm
from app.firebase_service import get_users, get_todos


app = create_app()

#todos = ['Mandar diseños navidad', 'Cerrar trato con proveedor', 'Entregar avances Break Food']

@app.cli.command()
def test():
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)

@app.route('/')
def home():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response

#importante respetar orden de los decoradores
@app.route('/hello', methods=['GET'])
@login_required
def hello():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    user_ip = session.get('user_ip')
    username = current_user.id

    context = {
        'user_ip': user_ip,
        'todos': get_todos(username=username),
        'username': username
    }

    users = get_users()
    for user in users:
        print(user.id)

    return render_template('hello.html', **context)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error= error)


if __name__ == '__main__':
    app.run(debug=True)
