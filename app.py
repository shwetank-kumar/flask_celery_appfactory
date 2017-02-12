from flask import Flask
from mod_add.views import add

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    app.register_blueprint(add)
    return app
