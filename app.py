from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, policy

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///policies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


migrate=Migrate(app, db)
# Initialize the sqlalchemy instance with flask app
db.init_app(app)

# Ensure that the flask application only runs when the script is executed directly
if __name__=='__main__':
    app.run(port=5000, debug=True)