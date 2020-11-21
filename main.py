from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
boostrap = Bootstrap(app)

todos = ['Mandar diseños navidad', 'Cerrar trato con proveedor', 'Entregar avances Break Food']

@app.route('/')
def home():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')

    context = {
        'user_ip': user_ip,
        'todos': todos
    }

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
