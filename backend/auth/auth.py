from flask import Blueprint, request, jsonify
from .models import User
from .utils import generate_token, verify_token

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401
    token = generate_token(user.id)
    return jsonify({'token': token})

@auth.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'})

@auth.route('/verify', methods=['POST'])
def verify():
    token = request.json.get('token')
    user_id = verify_token(token)
    if user_id is None:
        return jsonify({'error': 'Invalid token'}), 401
    user = User.query.get(user_id)
    return jsonify({'user': user.to_json()})
