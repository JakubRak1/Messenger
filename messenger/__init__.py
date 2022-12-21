import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@db:5432/postgres"
app.config['SECRET_KEY'] = '532f7ffa0a70512660d0bc83ad3388c1'

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from messenger.models import People, MessagesSent, MessagesRecive

db.create_all()


from messenger.main.routes import main

app.register_blueprint(main)
