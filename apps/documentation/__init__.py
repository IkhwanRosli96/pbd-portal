from flask import Blueprint

document_bp = Blueprint(
    'document_blueprint',
    __name__,
    url_prefix=''
)