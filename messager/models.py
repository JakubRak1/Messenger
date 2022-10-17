from messager import db, app

class User(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    first_name = db.Column (db.String(50), nullable = False)
    last_name = db.Column (db.String(50), nullable = False)
    email = db.Column (db.String(100), unique = True, nullable = False)
    password = db.Column (db.String(50), nullable = False)
    recived_messages = db.relationship('Messages', backref = 'author', lazy = True)
    sent_messages = db.relationship('Messages', backref = 'reciver', lazy = True)
    

    def __repr__(self) -> str:
        return f"User id: {self.id}, first name: {self.first_name}, last name: {self.last_name}, email: {self.email}, password: {self.password}"


class Messages(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    content = db.Column (db.Text, nullable = False)
    


    def __repr__(self) -> str:
        return f"Messages id: {self.id} Content: {self.content} Author: {self.author} Reciver: {self.reciver}"

