from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, policy
from routes import Policies, PolicyByID
from flask_restful import Api

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///policies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


# Initialize the sqlalchemy instance with flask app
db.init_app(app)
migrate=Migrate(app, db)

api=Api(app)

api.add_resource(Policies, '/policies')   
api.add_resource(PolicyByID, '/policies/<int:id>')

# Ensure that the flask application only runs when the script is executed directly
if __name__=='__main__':
    app.run(port=5000, debug=True)