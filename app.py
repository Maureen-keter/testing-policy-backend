from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, policy

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///policies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False