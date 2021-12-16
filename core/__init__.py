# Installed
from flask import Flask

# Built in
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///../database.db')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

import views
from . import database
