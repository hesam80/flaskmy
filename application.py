from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a new Flask application
app = Flask(__name__)

# Set up SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////artists.db'
db = SQLAlchemy(app)

# Define a class for the Artist table
class  User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


