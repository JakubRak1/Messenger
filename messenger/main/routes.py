from flask import render_template, Blueprint, redirect, flash, url_for
from flask_login import login_user, login_required, current_user, logout_user
from messenger import db, app
from messenger.main.forms import LoginForm, CreateUser, CreateMessage, ReplyMessage
from messenger.models import User, MessagesSent, MessagesRecive

main = Blueprint('main', __name__)


@main.route('/', methods=["GET", "POST"])
@main.route('/home', methods=["GET", "POST"])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if(user and user.password == form.password.data):
            login_user(user)
            return redirect(url_for('main.messanger'))
        else:
            flash('Inccorect email or password try again')
    return render_template('home.html', form = form)


@main.route('/register', methods=["GET","POST"])
def register_account():
    form = CreateUser()
    return render_template('register.html', form = form)


@main.route('/messenger', methods=["GET","POST"])
@login_required
def messanger():
    send_messages = MessagesSent.query.filter_by(author_email = current_user.email).all()
    recived_messages = MessagesRecive.query.filter_by(reciver_email = current_user.email).all()
    email_recived = []
    for i in range(len(recived_messages)):
        email_to_reply = MessagesSent.query.filter_by(content = recived_messages[i].content).first()
        email_recived.append(email_to_reply.author_email) 
    return render_template('messanger.html', send_messages = send_messages, recived_messages = recived_messages, user = current_user, sender = email_recived)


@main.route('/messenger/logout', methods=["GET","POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@main.route('/messenger/new_message', methods=["GET", "POST"])
@login_required
def create_new_message():
    form = CreateMessage()
    if form.validate_on_submit():
        reciver = User.query.filter_by(email=form.reciver_email.data).first()
        if(reciver):
            new_message_sent = MessagesSent(content = form.content.data, author_email = current_user.email)
            new_message_recived = MessagesRecive(content = form.content.data, reciver_email = reciver.email)
            db.session.add_all([new_message_sent, new_message_recived])
            db.session.commit()
            return redirect(url_for('main.messanger'))
        else:
            flash('There is no user with that email')
    return render_template('create_message.html', form = form)


@main.route('/messenger/reply_<int:msg_recived_id>', methods=["GET","POST"])
@login_required
def reply(msg_recived_id):
    form = ReplyMessage()
    msg_recived = MessagesRecive.query.filter_by(id = msg_recived_id).first()
    msg_sended = MessagesSent.query.filter_by(content=msg_recived.content).first()
    reciver = User.query.filter_by(email=msg_sended.author_email).first()
    if form.validate_on_submit():
        new_message_sent = MessagesSent(content = form.content.data, author_email = current_user.email)
        new_message_recived = MessagesRecive(content = form.content.data, reciver_email = reciver.email)
        db.session.add_all([new_message_sent, new_message_recived])
        db.session.commit()
        return redirect(url_for('main.messanger'))
    return render_template('reply.html', form=form)