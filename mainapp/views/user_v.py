from flask import Blueprint
from flask import request, render_template

blue = Blueprint('userBlue', __name__)


@blue.route('/login', methods=['POST', 'GET'])
def login():
    data = {
        'cookies':request.cookies,
        'base_url':request.base_url

    }
    return render_template('user/login.html',**data)
