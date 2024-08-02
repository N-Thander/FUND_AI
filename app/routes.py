from flask import Blueprint, render_template, request, jsonify, url_for, redirect, flash
from .models import db, UserProfileData
from werkzeug.security import generate_password_hash
from .forms import SignUp


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = SignUp()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email_id = form.email.data
        contact_number = form.contact_number.data
        password = form.password.data
        name = first_name + " " + last_name
        new_user_id = UserProfileData.generate_user_id()
        hashed_password = generate_password_hash(password, method='sha256')
        
        new_user = UserProfileData(user_id=new_user_id, name=name, email_id=email_id, contact_number=contact_number, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('User Added Successfully')
        return redirect(url_for('main.index'))

    return render_template('sign_up.html', form=form)


"""
@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email_id = data.get('email_id')
    password = data.get('password')
    
    user = UserProfileData.query.filter_by(email_id=email_id).first()
    
    if user and check_password_hash(user.password, password):
        return jsonify({"messege": "login Successfu", "user_id": user.user_id, "name":user.name}), 200
    else:
        return jsonify({"messege": "Invalid Email or Password"}), 401    
"""   
