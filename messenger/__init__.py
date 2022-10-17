from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///message.db'
app.config['SECRET_KEY'] = '532f7ffa0a70512660d0bc83ad3388c1'

db = SQLAlchemy(app)


from messenger.main.routes import main

app.register_blueprint(main)