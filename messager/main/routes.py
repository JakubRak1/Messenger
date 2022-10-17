from flask import render_template, Blueprint, redirect, flash, url_for
from messager import db, app
from messager.main.forms import LoginForm, CreateUser
from messager.models import User
from flask_login import login_user

main = Blueprint('main', __name__)


@main.route('/', methods=["GET", "POST"])
@main.route('/home', methods=["GET", "POST"])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.data).first()
        if(user and user.password == form.password):
            login_user(user)
            return redirect(url_for(main.messanger))
        else:
            flash('Inccorect email or password try again')
    return render_template('home.html', form = form)

@main.route('/register', methods=["GET","POST"])
def register_account():
    form = CreateUser()
    return render_template('register.html', form = form)


@main.route('/messanger', methods=["GET","POST"])
def messanger():
    form = CreateUser()
    return render_template('register.html', form=form)
