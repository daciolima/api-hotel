from flask import Flask
from dynaconf import FlaskDynaconf
from flask_restful import Api
from resources.hotel import Hoteis
from resources.hotel import Hotel
from sql_alchemy import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
FlaskDynaconf(app)
api = Api(app)
db.init_app(app)


@app.before_first_request
def cria_banco():
    db.create_all()


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hotel/<int:hotel_id>')


if __name__ == '__main__':
    app.run()

