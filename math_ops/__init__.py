from celery import Celery
from flask import Flask
from config import config, DevelopmentConfig

celery = Celery(__name__, broker=DevelopmentConfig.broker_url,
                backend=DevelopmentConfig.result_backend)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    celery.conf.update(app.config)

    from .mod_add import mod_add as mod_add_bp
    # app.register_blueprint(mod_add_bp, url_prefix="/add)
    app.register_blueprint(mod_add_bp)

    return app
