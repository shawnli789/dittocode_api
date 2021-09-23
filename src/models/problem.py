from db import db
from datetime import datetime
from models.user import User

class Problem(db.Model):
    __tablename__ = 'problem'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(30), nullable=False)
    difficulty = db.Column(db.String(30), nullable=False)
    tags = db.Column(db.String(300), nullable=False)
    completed= db.Column(db.Boolean, nullable=False)
    url= db.Column(db.String(3000), nullable=True)
    time_spent = db.Column(db.Integer, nullable=False)

    def __init__(self, **kwargs):
        self.user_id = kwargs["user_id"]
        self.number = kwargs["number"]
        self.title = kwargs["title"]
        self.type = kwargs["type"]
        self.difficulty = kwargs["difficulty"]
        self.tags = kwargs["tags"]
        self.completed = kwargs["completed"]
        self.url = kwargs.get("url")
        self.time_spent = kwargs.get("time_spent")

    def json(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'user_id': self.user_id,
            'number': self.number,
            'title': self.title,
            'type': self.type,
            'difficulty': self.difficulty,
            'tags': self.tags,
            'completed': self.completed,
            'url': self.url,
            'time_spent': self.time_spent,
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self, data):
        self.number = data["number"]
        self.title = data["title"]
        self.type = data["type"]
        self.difficulty = data["difficulty"]
        self.tags = data["tags"]
        self.completed = data["completed"]
        self.url = data.get("url")
        self.time_spent = data.get("time_spent")
        db.session.commit()
    


