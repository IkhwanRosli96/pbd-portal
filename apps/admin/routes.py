from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash
from flask_login import current_user, login_required

from apps.admin import admin_bp
from apps.admin.form import CreateUserForm, UpdatePasswordForm, UpdateUserForm, deleteUserForm

from apps.admin.util import get_permission
from apps.database.models import ApiUser
from datetime import datetime

@admin_bp.route('/user_management', methods=['GET'])
@login_required
def user_management():
    create_usr_form = CreateUserForm()
    update_pwd_form = UpdatePasswordForm()
    update_usr_form = UpdateUserForm()
    collections = ["Collection1", "Collection2", "Collection3"]

    if current_user.is_authenticated:
        login_log = current_user.login_log
        user = ApiUser.objects(login_log=login_log).first()

        if user:
            if user.privilege == 0:  # Super Admin
                # Super Admin sees all users
                users = ApiUser.objects()
            elif user.privilege == 1:  # Admin
                # Admin sees only normal users (privilege == 2)
                users = ApiUser.objects(privilege=2)
            else:
                # Unauthorized access, redirect to logout
                return redirect(url_for('logout_blueprint.logout'))

            return render_template(
                'management/user/user_management.html',
                users=users,
                username=user.username,
                update_pwd_form=update_pwd_form,
                create_usr_form=create_usr_form,
                update_usr_form=update_usr_form,
                collections=collections
            )
        else:
            return redirect(url_for('logout_blueprint.logout'))
    else:
        return redirect(url_for('logout_blueprint.logout'))



@admin_bp.route('/create_user', methods=['POST'])
@login_required
def create_user():
    form = CreateUserForm()
    if current_user.is_authenticated:
        login_log = current_user.login_log
        user = ApiUser.objects(login_log=login_log).first()

        if user:
            if user.privilege < 1 and form.validate_on_submit():
                username = form.username.data
                password = form.password.data
                privilege = int(form.privilege.data)
                allowed_collections = request.form.getlist('collections') if 'collections' in request.form else []

                # Default to all collections if no selection made
                if 'access-type' in request.form and request.form['access-type'] == 'ALL':
                    allowed_collections = ['ALL']
                
                created_user = ApiUser(
                    username=username,
                    password=password,
                    privilege=privilege,
                    allowed_collection=allowed_collections or ['ALL'],
                    is_activate=True
                )
                created_user.hash_password()
                created_user.save()

                flash("[SUCCESS] User Successfully Created!", "user_creation_valid")
                return redirect(url_for('admin_blueprint.user_management'))
            else:
                flash("[ERROR] User Creation Failed! Invalid Data.", "user_creation_invalid")
                return redirect(url_for('admin_blueprint.user_management'))
    return redirect(url_for('logout_blueprint.logout'))


@admin_bp.route('/update_user', methods=['POST'])
@login_required
def update_user():
    form = UpdateUserForm()
    if current_user.is_authenticated:
        username = form.username.data
        selected_username = form.selected_user.data
        privilege = form.privilege.data
        permisson = get_permission(int(privilege))


        login_log = current_user.login_log
        user = ApiUser.objects(login_log=login_log).first()

        if user:
            check_user_exist = ApiUser.objects(username=selected_username).first()
            if check_user_exist:
                check_user_exist.update(set__username=username, set__privilege=privilege, set__allowed_action=permisson)
                check_user_exist.save()

                flash("[SUCCESS] Succesful Updating the User!", "user_update_valid")
                return redirect(url_for('admin_blueprint.user_management'))
            else:
                flash("[ERROR] Updating User Failed! User Does Not Exist.", "user_creation_invalid")
                return redirect(url_for('admin_blueprint.user_management'))
        else:
            return redirect(url_for('logout_blueprint.logout'))
    else:
        return redirect(url_for('logout_blueprint.logout'))

@admin_bp.route('/change_password', methods=['POST'])
@login_required
def change_password():
    form = UpdatePasswordForm()
    if current_user.is_authenticated:
        username = form.username.data
        password = form.current_pwd.data
        new_pwd = form.new_pwd.data

        login_log = current_user.login_log
        user = ApiUser.objects(login_log=login_log).first()
        
        if user:
            check_user_exist = ApiUser.objects(username=user.username).first()
            if check_user_exist.check_password(password):
                if form.validate_on_submit():

                    updated_user = ApiUser.objects(username=username).first()
                    updated_user.update(set__password=new_pwd)
                    updated_user.hash_password()
                    updated_user.save()

                    if user.username == updated_user.username:
                        flash("Password succesfully changed. Please login using the new password", "pass_change")
                        return redirect(url_for('logout_blueprint.logout'))
                    else:
                        flash("Password succesfully changed.", "pass_change")
                        return redirect(url_for('admin_blueprint.user_management'))
                else:
                    flash("The new password and confirmation password is not the same.", "not_same_pass")
                    return redirect(url_for('admin_blueprint.user_management'))
            else:
                flash("Your password is incorrect.")
                return redirect(url_for('admin_blueprint.user_management'))
        else:
            return redirect(url_for('logout_blueprint.logout'))
    else:
        return redirect(url_for('logout_blueprint.logout'))


@admin_bp.route('/delete_user', methods=['POST'])
@login_required
def delete_user():
    if current_user.is_authenticated:
        username = request.form.get('username')

        login_log = current_user.login_log
        user =  ApiUser.objects(login_log=login_log).first()

        current_username = user.username

        if user:
            if user.privilege == 1:
                check_user_exist = ApiUser.objects(username=username).first()

                if check_user_exist is not None:
                    deleted_username = check_user_exist.username
                    ApiUser.objects.get(username=deleted_username).delete()

                    if current_username == deleted_username:
                        return redirect(url_for('logout_blueprint.logout'))
                    else:
                        return redirect(url_for('admin_blueprint.user_management'))
            else:
                return redirect(url_for('logout_blueprint.logout'))
        else:
            return redirect(url_for('logout_blueprint.logout'))
    else:
        return redirect(url_for('logout_blueprint.logout'))