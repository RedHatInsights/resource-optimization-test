# app.py
from flask import Flask

import os

app = Flask(__name__)


@app.route('/')
def marzipan_index():
    greeting = os.environ.get('GREETING', 'Hi!')
    return f'{greeting} This is test app\n'
