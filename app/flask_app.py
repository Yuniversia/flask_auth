from app.db import crt_usr, get_usr, get_psw

from flask import Blueprint, request, jsonify

auth = Blueprint('backend', __name__)

@auth.route("/")
def root():
    return 'root'

@auth.route("/login", methods=['POST'])
def login():
    try:
        data = request.form
        name = data['name']
        psw = data['psw']
        num = data['num']

        res = crt_usr(name, num, psw)

        if not res[0]:
            return jsonify({'err': f"{res[1]}"}), 500

        return jsonify({'res': f"{res[1]}"}), 200

    except Exception as e:
        return jsonify({'err': e}), 500
    
@auth.route("/user/<name>", methods=['GET'])
def get_user(name):
    try:
        res = get_usr(name)

        return jsonify({'usr_id': f"{res.id}", 'usr_name' : f'{res.name}'}), 200

    except Exception as e:
        return jsonify({'err': e}), 500
    
@auth.route("/login/<name>", methods=['POST'])
def log_in(name):
    try:
        data = request.form
        psw = data['psw']
        res = get_psw(name, psw)

        return jsonify({'res': res}), 200

    except Exception as e:
        return jsonify({'err': e}), 500

@auth.route("/favicon.ico")
def icon():
    return '', 404