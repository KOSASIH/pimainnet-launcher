from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('payments', lazy=True))
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(64), nullable=False)
    payment_status = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f'<Payment {self.id}>'
