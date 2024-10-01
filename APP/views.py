import flask
from flask import render_template, Blueprint, request

blue = Blueprint('user', __name__)


@blue.route('/')
@blue.route('/index')
def index():
    return render_template('index.html', name='flask')


@blue.route('/getuuid/')
def getuuid():
    import uuid
    return str(uuid.uuid4())


@blue.route('/request/', methods=['GET', 'POST'])
def get_request():
    print('url:' + request.url)
    print('base_url:' + request.base_url)
    print('host:' + request.host)
    print('host_url:' + request.host_url)
    print(request.args)
    print(request.form)
    print(request.path)
    print(request.remote_addr)
    print(request.remote_user)
    print(request.method)
    print(request.files)
    print(request.cookies)
    print(request.headers)
    return '200 OK'


@blue.route('/redirect/')
def get_redirect():
    return flask.redirect('/index')
    pass


@blue.route('/login/')
def login():
    # GET
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        pass
