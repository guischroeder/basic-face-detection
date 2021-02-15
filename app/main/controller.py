from flask import Blueprint

bp = Blueprint('controller', __name__)

@bp.route('/', methods=["GET"])
def get():
  return 'Hello!'