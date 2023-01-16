import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from messenger.models import MessagesRecive, MessagesSent, People

db.create_all()


from messenger.main.routes import main

app.register_blueprint(main)
