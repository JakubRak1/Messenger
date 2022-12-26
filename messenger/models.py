from messenger import db, app, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return People.query.get(int(user_id))


class People(db.Model, UserMixin):
    __name__ = "People"
    id = db.Column (db.Integer, primary_key = True)
    first_name = db.Column (db.String(50), nullable = False)
    last_name = db.Column (db.String(50), nullable = False)
    email = db.Column (db.String(100), unique = True, nullable = False)
    password = db.Column (db.String(50), nullable = False)
    message_created = db.relationship('MessagesSent', backref = 'people', lazy = True)
    message_recived = db.relationship('MessagesRecive', backref = 'people', lazy = True)
    message_send_display = db.relationship('MessagesSentDisplay', backref = 'people', lazy = True)
    

    def __repr__(self) -> str:
        return f"User id: {self.id}, first name: {self.first_name}, last name: {self.last_name}, email: {self.email}, password: {self.password}"
    

    def __init__(self, first_name, last_name, email, password, message_created, message_recived, message_send_display):
        self.first_name = first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.message_created=message_created
        self.message_recived=message_recived
        self.message_send_display=message_send_display


class MessagesSent(db.Model):
    __name__="MessagesSent"
    id = db.Column (db.Integer, primary_key = True)
    content = db.Column (db.Text, nullable = False)
    author_email = db.Column (db.String(50), db.ForeignKey('people.email'))
  

    def __repr__(self) -> str:
        return f"Messages sended id: {self.id} Content: {self.content} Author: {self.author_email}"


    def __init__(self, content, author_email):
        self.content=content
        self.author_email=author_email


class MessagesRecive(db.Model):
    __name__ = "MessagesRecive"
    id = db.Column (db.Integer, primary_key = True)
    content = db.Column (db.Text, nullable = False)
    reciver_email = db.Column (db.String(50), db.ForeignKey('people.email'))
    

    def __repr__(self) -> str:
        return f"Messages incoming id: {self.id} Content: {self.content} Reciver: {self.reciver_email}"


    def __init__(self, content, reciver_email):
        self.content=content
        self.reciver_email=reciver_email

class MessagesSentDisplay(db.Model):
    __name__ = "MessagesSentDisplay"
    id = db.Column (db.Integer, primary_key = True)
    content = db.Column (db.Text, nullable = False)
    author_email = db.Column (db.String(50), db.ForeignKey('people.email'))
    reciver_email = db.Column (db.String(100), nullable = False)

    def __repr__(self) -> str:
        return f"Messages sended in local mailbox id: {self.id} Content: {self.content} Author: {self.author_email}"


    def __init__(self, content, author_email, reciver_email):
        self.content=content
        self.author_email=author_email
        self.reciver_email=reciver_email