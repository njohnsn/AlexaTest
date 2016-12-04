from flask import Flask
from config import config
from flask_ask import Ask

ask = Ask()
ask._route = "/alexa_1_0"

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    ask.init_app(app)

    if not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .alexa_1_0 import alexa as alexa_1_0_blueprint
    app.register_blueprint(alexa_1_0_blueprint)

    return app
