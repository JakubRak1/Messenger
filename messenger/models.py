from messenger import db, app, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column (db.Integer, primary_key = True)
    first_name = db.Column (db.String(50), nullable = False)
    last_name = db.Column (db.String(50), nullable = False)
    email = db.Column (db.String(100), unique = True, nullable = False)
    password = db.Column (db.String(50), nullable = False)
    message_created = db.relationship('MessagesSent', backref = 'user', lazy = True)
    message_recived = db.relationship('MessagesRecive', backref = 'user', lazy = True)
    

    def __repr__(self) -> str:
        return f"User id: {self.id}, first name: {self.first_name}, last name: {self.last_name}, email: {self.email}, password: {self.password}"


class MessagesSent(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    content = db.Column (db.Text, nullable = False)
    author_email = db.Column (db.Integer, db.ForeignKey('user.email'))
  

    def __repr__(self) -> str:
        return f"Messages sended id: {self.id} Content: {self.content} Author: {self.author_email}"


class MessagesRecive(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    content = db.Column (db.Text, nullable = False)
    reciver_email = db.Column (db.Integer, db.ForeignKey('user.email'))
    

    def __repr__(self) -> str:
        return f"Messages incoming id: {self.id} Content: {self.content} Reciver: {self.reciver_email}"

