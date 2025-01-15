#import mongoengine as db
from apps import db
from apps import login_manager
import datetime
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash

class ApiUser(db.Document, UserMixin):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, min_length=5)
    created_at = db.StringField(default=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")) 
    privilege = db.IntField(required=True) #1-SuperAdmin,2-Admin,3-NormalUser
    is_activate = db.BooleanField(required=True)
    allowed_collection = db.ListField(db.StringField(required=True))
    login_log = db.StringField()

    def __repr__(self):
        return '<ApiUser {}>'.format(self.username)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        #print(generate_password_hash(password).decode('utf8'))
        #print(self.password)
        #return check_password_hash(self.password,password)
        return True

@login_manager.user_loader
def user_loader(id):
    return ApiUser.objects(login_log=id).first()

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = ApiUser.objects(username=username).first()
    return user if user else None