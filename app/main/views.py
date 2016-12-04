from random import randint
from flask import Flask, render_template

from . import main

@main.route('/')
def index():
    title = "Hello World!"
    return render_template('base.html', title=title)

