from sql_alchemy import db
from flask import request, url_for
from requests import post
import datetime

MAILGUN_DOMAIN = ''
MAILGUN_API_KEY = ''
FROM_TITLE = ''
FROM_EMAIL = ''


class UserModel(db.Model):

    __tablename__ = 'usuario'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)
    status = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, name, username, email, password, status):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.status = status

    def json(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "status": self.status
        }

    def send_confimation_email(self):
        link = request.url_root[:-1] + url_for('userconfirm', user_id=self.user_id)
        return post('https://api.mailgun.net/v3/{}/messages'.format(MAILGUN_DOMAIN),
                    auth=('api', MAILGUN_API_KEY),
                    data={'from': '{} <{}>'.format(FROM_TITLE, FROM_EMAIL),
                          'to': self.email,
                          'subject': 'Confirmação do cadastro.',
                          'text': 'Confirme seu cadastro clicando no link a seguir: {}'.format(link),
                          'html': '<html><p>Confirme o cadastro clicando no link: <a href="{}" target="blank">'
                                  'Confirmar cadastro</a></p></html>'.format(link)}
                    )


    @classmethod
    def find_user_by_usename(cls, user_username):
        user = cls.query.filter_by(username=user_username).first()
        if user:
            return user
        return None

    @classmethod
    def find_email(cls, user_email):
        user = cls.query.filter_by(email=user_email).first()
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

    def update_user(self, name, username, password, status):
        self.name = name
        self.username = username
        self.password = password
        self.status = status

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
