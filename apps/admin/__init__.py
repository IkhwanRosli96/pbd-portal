from flask import Blueprint

admin_bp = Blueprint(
    'admin_blueprint',
    __name__,
    url_prefix=''
)
