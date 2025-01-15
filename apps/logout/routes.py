from flask import redirect, url_for, session
from flask_login import logout_user

from apps import db

from apps.logout import logout_bp

@logout_bp.route('/', methods=['GET', 'POST'])
def logout():
    logout_user()
    session["username"] = None
    return redirect(url_for('login_blueprint.login'))