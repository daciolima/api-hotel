from flask import Flask
from dynaconf import FlaskDynaconf
from flask_restful import Api
from resources.hotel import Hoteis

app = Flask(__name__)
FlaskDynaconf(app)
api = Api(app)


api.add_resource(Hoteis, '/hoteis')


if __name__ == '__main__':
    app.run()

