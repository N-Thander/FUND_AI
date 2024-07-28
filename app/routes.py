from flask import Blueprint, request, jsonify
from .models import db, UserData
from werkzeug.security import check_password_hash

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "FUND_AI"

# following here add functions accordingly 

@main.route('/sign_in', methods=['POST'])
def sign_in():
    data = request.get_json()
    new_user_id = UserData.gererate_user_id()
    new_user = UserData(user_id=new_user_id, name=data['name'], email_id=data['email_id'], contact_number=data['contact_number'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"messege": "User Added Successfully", "UserID": new_user_id}), 201


@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email_id = data.get('email_id')
    password = data.get('password')
    
    user = UserData.query.filter_by(email_id=email_id).first()
    
    if user and check_password_hash(user.password, password):
        return jsonify({"messege": "login Successfu", "user_id": user.user_id, "name":user.name}), 200
    else:
        return jsonify({"messege": "Invalid Email or Password"}), 401
    
    
