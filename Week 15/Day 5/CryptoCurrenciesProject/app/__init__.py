import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# import os

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY SECRET KEY'
app.config['DEBUG'] = True
# os.system('export FLASK_APP=run.py')

# Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/CryptoCurrenciesProject"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure Flask Login
login = LoginManager(app)
login.init_app(app)
login.session_protection = "strong"


@login.user_loader
def load_user(userid):
    return models.Users.query.get(int(userid))


from app import models, routes
