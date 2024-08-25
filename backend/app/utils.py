import jwt
from flask import current_app

def generate_token(user_id):
    payload = {'user_id': user_id}
    return jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')

def verify_token(token):
    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def error_handler(status_code, message):
    return jsonify({'error': message}), status_code
