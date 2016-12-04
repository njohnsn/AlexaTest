from flask import Flask, render_template, current_app
from config import config

from random import randint

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .alexa import ask
    ask._route = '/alexa_1_0/'
    ask.init_app(app)

    if not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

