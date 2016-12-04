from flask import Blueprint
from flask_ask import Ask

alexa = Blueprint('alexa', __name__)

from . import views
