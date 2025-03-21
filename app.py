from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db=SQLAlchemy()


class Policy(db.Model, SerializerMixin)
    __tablename__='policies'
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(100), nullable=False)  # Policy name
    type = db.Column(db.String(50), nullable=False)  # Policy type
    premium = db.Column(db.Float, nullable=False)  # Premium amount
    status = db.Column(db.String(20), default="active")