from flask import Flask
from dynaconf import FlaskDynaconf
from flask_restful import Api
from resources.hotel import Hoteis
from resources.hotel import Hotel

app = Flask(__name__)
FlaskDynaconf(app)
api = Api(app)


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hotel/<int:hotel_id>')


if __name__ == '__main__':
    app.run()

