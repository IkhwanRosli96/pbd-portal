from flask import render_template, redirect, url_for, flash
from flask_login import login_user, UserMixin

from apps import db, logger
from apps.login.form import LoginForm
from apps.login import login_bp
from apps.login.util import id_generator
from apps.database.models import ApiUser

class User(UserMixin):
    pass

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm() 
    if form.validate_on_submit(): 
        username = form.username.data 
        password = form.password.data 
        randomid = id_generator()

        try:
            user = ApiUser.objects(username=username).first()
        except Exception as e:
            print(e)
            user = None

        if user:
            if user.check_password(password):
                user.login_log = randomid
                user.update(set__login_log=str(randomid))

                user_login = User()
                user_login.id = randomid
                login_user(user_login)

                logger.warning("[INFO] [LOGIN] {} logging in...".format(user.username))

                if user.privilege < 3:
                    flash('You were successfully logged in', 'rightadmin')
                    return redirect(url_for('admin_blueprint.user_management'))
                else:
                    flash('You were successfully logged in as user', 'rightuser')
                    return redirect(url_for('user_blueprint.dashboard'))
            else:
                print("2")
                flash("Wrong Username or Password. Try again!", "wrong_cred")
                return render_template("accounts/login.html", form=form)
        else:
            print("1")
            flash("Wrong Username or Password. Try again!","wrong_cred")
            return render_template("accounts/login.html", form=form)
    else:
        return render_template("accounts/login.html", form=form)
        