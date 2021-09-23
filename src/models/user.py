from datetime import datetime
from db import db
from enum import unique
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


    def __init__(self, **kwargs):
        self.username = kwargs["username"]
        self.email = kwargs["email"]
        self.password = kwargs["password"]
        
    def json(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'username': self.username,
            'email': self.email, 
        }
    
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        self.username = data["username"]
        self.email = data["email"]
        self.password = data["password"]
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()



    

        
