from .db import db

from flask import Flask

def get_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'

    db.init_app(app)

    from app.flask_app import auth

    app.register_blueprint(auth)
    
    return app

if __name__ == '__main__':
    app = get_app()
    app.run(debug=True)