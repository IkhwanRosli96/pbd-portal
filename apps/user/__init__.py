from flask import Blueprint

user_bp = Blueprint(
    'user_blueprint',
    __name__,
    url_prefix=''
)