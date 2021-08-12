from flask import Flask
from dynaconf import FlaskDynaconf
from flask_restful import Resource, Api

app = Flask(__name__)
FlaskDynaconf(app)
api = Api(app)


class Hoteis(Resource):
    def get(self):
        return {'hoteis': 'meus hoteis'}


api.add_resource(Hoteis, '/hoteis')


if __name__ == '__main__':
    app.run()

