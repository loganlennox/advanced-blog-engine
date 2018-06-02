from flask import Flask

# Define the WSGI application object
app = Flask(__name__)

# Add configuration from config.py
app.config.from_object("config")

# Import basic routes
from app import views
