from flask import Blueprint, render_template, request, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

# need to complete the log in page
@main.route('/login', methods=['GET'])
def login():
    pass