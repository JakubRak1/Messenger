from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = '532f7ffa0a70512660d0bc83ad3388c0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_BINDS'] = {'two': 'sqlite:///tokens.db'}
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
