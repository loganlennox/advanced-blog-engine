# Enable development environment
DEBUG = True

# Define root directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database
SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/blogtest"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Application threads
THREADS_PER_PAGE = 2

# Secret key
SECRET_KEY = "secretkey"
