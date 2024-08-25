from flask import Blueprint, request, jsonify
from .services import auth_service, payment_service
from .models import User, Payment
from .utils import error_handler

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_json() for user in users])

@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return error_handler(404, 'User not found')
    return jsonify(user.to_json())

@api.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([payment.to_json() for payment in payments])

@api.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment is None:
        return error_handler(404, 'Payment not found')
    return jsonify(payment.to_json())

@api.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = auth_service.authenticate(username, password)
    if user is None:
        return error_handler(401, 'Invalid credentials')
    token = auth_service.generate_token(user)
    return jsonify({'token': token})

@api.route('/payments', methods=['POST'])
def create_payment():
    user_id = request.json.get('user_id')
    amount = request.json.get('amount')
    payment_method = request.json.get('payment_method')
    payment_status = request.json.get('payment_status')
    payment = payment_service.create_payment(user_id, amount, payment_method, payment_status)
    return jsonify(payment.to_json())

@api.route('/payments/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment is None:
        return error_handler(404, 'Payment not found')
    payment.amount = request.json.get('amount')
    payment.payment_method = request.json.get('payment_method')
    payment.payment_status = request.json.get('payment_status')
    payment_service.update_payment(payment)
    return jsonify(payment.to_json())

@api.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment is None:
        return error_handler(404, 'Payment not found')
    payment_service.delete_payment(payment)
    return jsonify({'message': 'Payment deleted'})
