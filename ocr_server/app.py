import logging
import uuid

import envpy
from flask import (
    Flask,
    abort,
    jsonify,
    make_response,
    redirect,
    request,
    render_template
)

app = Flask(__name__)

CONFIG = envpy.get_config({
    'PORT': envpy.Schema(
        value_type=int,
        default=8000,
    ),
    'LOG_LEVEL': envpy.Schema(
        value_type=str,
        default='INFO',
    ),
})

SECRETS = envpy.get_config({
    'QUESTION': envpy.Schema(
        value_type=str,
        default=None,
    ),
    'ANSWER': envpy.Schema(
        value_type=str,
        default=None,
    ),
})


def init():
    # Init logging
    logging_handler = logging.StreamHandler()
    logging_formatter = logging.Formatter(\
        "%(asctime)s - %(levelname)s - %(name)s: %(message)s")
    logging_handler.setFormatter(logging_formatter)
    app.logger.addHandler(logging_handler)

    level = CONFIG['LOG_LEVEL'].upper()
    if level == 'DEBUG':
        app.logger.setLevel(logging.DEBUG)
    elif level == 'INFO':
        app.logger.setLevel(logging.INFO)

    # Log current config
    app.logger.info('Config loaded: %s', CONFIG)

init()


@app.route('/', methods=['GET'])
def index():
    error = None
    if not SECRETS['QUESTION']:
        error = 'Question not set'
    elif not SECRETS['ANSWER']:
        error = 'Answer not set'

    return render_template(
        'index.html',
        question=SECRETS['QUESTION'],
        error=error,
    )

@app.route('/answer', methods=['POST', 'GET'])
def answer():
    correct = False
    if request.method == 'POST':
        correct = request.form.get('answer') == SECRETS['ANSWER']
    return render_template(
        'answer.html',
        correct=correct,
    )
