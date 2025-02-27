from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    equipment = db.relationship('Equipment', backref='hike', lazy=True)

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    hike_id = db.Column(db.Integer, db.ForeignKey('hike.id'), nullable=False)