import logging
import json

from werkzeug.exceptions import HTTPException


def handle_error(e):
    code = 500

    if isinstance(e, HTTPException):
        code = e.code

    error_message = str(e)

    logging.error(error_message)

    return json.dumps({"error": error_message}), code
