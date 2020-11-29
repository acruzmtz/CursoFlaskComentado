from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest
from flask_login import login_required, current_user
from app import create_app
from app.forms import TodoForm, DeleteTodoForm, UpdateTodoForm
from app.firebase_service import get_users, get_todos, add_todo, delete, update_todo


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
@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    delete_todo = DeleteTodoForm()
    update_todo = UpdateTodoForm()

    context = {
        'user_ip': user_ip,
        'todos': get_todos(username=username),
        'username': username,
        'todo_form': todo_form,
        'delete_todo': delete_todo,
        'update_todo': update_todo
    }

    if todo_form.validate_on_submit():
        description = todo_form.description.data
        add_todo(username, description)

        flash('La tarea se creo correctamente')

        return redirect(url_for('hello'))

    return render_template('hello.html', **context)


@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete_todo(todo_id):
    user_id = current_user.id
    delete(user_id=user_id, todo_id=todo_id)

    return redirect(url_for('hello'))


@app.route('/todos/update/<todo_id>/<int:done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id
    update_todo(user_id=user_id, todo_id=todo_id, done=done)

    return redirect(url_for('hello'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error= error)


if __name__ == '__main__':
    app.run(debug=True)
