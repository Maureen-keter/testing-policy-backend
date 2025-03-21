from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db=SQLAlchemy()


class Policy(db.Model, SerializerMixin)
    __tablename__='policies'