from database import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    avatar = db.Column(db.String(100), nullable=True)
    favorites = db.relationship('ForeignCelebrities', secondary='favorites', backref=db.backref('users', lazy='dynamic'))

