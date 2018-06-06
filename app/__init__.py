from flask import Flask

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Add configuration from config.py
app.config.from_object("config")

# Define database object
db = SQLAlchemy(app)

# Import controllers
from app import controllers

# Import module(s)
from app.mod_auth.controllers import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)

# Build database
db.create_all()
