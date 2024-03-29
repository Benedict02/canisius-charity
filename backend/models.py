from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(50), primary_key=True)
    owned_seat = db.relationship('Seat', backref='owner', lazy=True)

    def __init__(self, id):
        self.id = id

class Seat(db.Model):
    __tablename__ = "seats"
    id = db.Column(db.String(3), primary_key=True)
    isAvailable = db.Column(db.Boolean, nullable=False)
    isVIP = db.Column(db.Boolean, nullable=False)
    owner_id = db.Column(db.String(50), db.ForeignKey('users.id'))

    def __init__(self, id, isAvailable, isVIP, owner_id):
        self.id = id
        self.isAvailable = isAvailable
        self.isVIP = isVIP
        self.owner_id = owner_id