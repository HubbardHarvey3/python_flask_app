from flask import Flask, request, url_for, render_template, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html.jinja')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Send the Login : POST"
    else:
        return "Get the login : GET"


@app.route('/user/')
@app.route('/user/<name>')
def hello(name=None):
    return render_template('index.html.jinja', name=name)
