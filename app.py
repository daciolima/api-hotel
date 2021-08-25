from flask import Flask, jsonify
from dynaconf import FlaskDynaconf
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.site import Site, Sites
from resources.usuario import UserAll, User, UserRegister, UserLogin, UserLogout
from sql_alchemy import db
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DXk*d}&2hwA9pA&'
app.config['JWT_BLACKLIST_ENABLED'] = True
FlaskDynaconf(app)
jwt = JWTManager(app)
api = Api(app)
db.init_app(app)


@app.before_first_request
def cria_banco():
    db.create_all()


@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'message': 'Vocè já saiu'}), 401


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hotel/<int:hotel_id>')
api.add_resource(UserAll, '/usuarios')
api.add_resource(UserRegister, '/usuarios')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(Sites, '/sites')
api.add_resource(Site, '/sites/<string:url>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')


if __name__ == '__main__':
    app.run()

