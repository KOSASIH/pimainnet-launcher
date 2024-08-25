from .models import User, Payment
from .utils import generate_token, verify_token

class AuthService:
    def authenticate(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return None
        return user

    def generate_token(self, user):
        return generate_token(user.id)

    def verify_token(self, token):
        return verify_token(token)

class PaymentService:
    def create_payment(self, user_id, amount, payment_method, payment_status):
        payment = Payment(user_id=user_id, amount=amount, payment_method=payment_method, payment_status=payment_status)
        db.session.add(payment)
        db.session.commit()
        return payment

    def update_payment(self, payment):
        db.session.commit()
        return payment

    def delete_payment(self, payment):
        db.session.delete(payment)
        db.session.commit()
