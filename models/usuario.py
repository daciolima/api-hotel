from sql_alchemy import db
import datetime


class UserModel(db.Model):

    __tablename__ = 'usuario'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    username = db.Column(db.String(20))
    password = db.Column(db.String(25))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def json(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "username": self.username,
        }

    @classmethod
    def find_user_by_usename(cls, user_username):
        user = cls.query.filter_by(username=user_username).first()
        if user:
            return user
        return None

    @classmethod
    def find_user_by_id(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        return None

    @classmethod
    def user_all(cls):
        users = cls.query.all()
        if users:
            return users
        return None

    def update_user(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
