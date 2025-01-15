from flask import render_template, redirect, url_for, request, jsonify, flash
from flask_login import current_user, logout_user, login_required

from apps import db
from apps.documentation import document_bp

import csv
import os

@document_bp.route('/documentation', methods=['GET'])
def documentation():
     return "Documentation"

     
