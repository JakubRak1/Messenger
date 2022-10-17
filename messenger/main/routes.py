from flask import render_template, Blueprint, redirect, flash, url_for
from messenger import db, app
from messenger.main.forms import LoginForm, CreateUser, CreateMessage
from messenger.models import User, MessagesSent, MessagesRecive

main = Blueprint('main', __name__)


@main.route('/', methods=["GET", "POST"])
@main.route('/home', methods=["GET", "POST"])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if(user and user.password == form.password.data):
            return redirect(url_for('main.messanger'))
        else:
            flash('Inccorect email or password try again')
    return render_template('home.html', form = form)

@main.route('/register', methods=["GET","POST"])
def register_account():
    form = CreateUser()
    return render_template('register.html', form = form)


@main.route('/messenger', methods=["GET","POST"])
def messanger():
    form = CreateUser()
    return render_template('register.html', form=form)
# do dopisania messenger aplikacja 
