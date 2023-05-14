from flask import Blueprint, render_template

route = Blueprint('route', __name__, url_prefix='/')

@route.route('/')
def index():
    return render_template('index.html')