from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///message.db'
app.config['SECRET_KEY'] = '532f7ffa0a70512660d0bc83ad3388c1'

db = SQLAlchemy(app)


from messager.main.routes import main

app.register_blueprint(main)
