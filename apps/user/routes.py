from flask import render_template, redirect, url_for, request, jsonify, flash
from flask_login import current_user, logout_user, login_required

from apps import db
from apps.user import user_bp

import csv
import os

@user_bp.route('/dashboard', methods=['GET'])
def dashboard():
     return "HELLO DASHBOARD"

     
