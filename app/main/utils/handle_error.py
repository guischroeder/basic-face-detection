import logging

from flask import jsonify
from werkzeug.exceptions import HTTPException


def handle_error(e):
    code = 500

    if isinstance(e, HTTPException):
        code = e.code

    error_message = str(e)

    logging.error(error_message)

    return jsonify(error=error_message), code
