from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from models.site import SiteModel
from flask_jwt_extended import jwt_required
import sqlite3
from resources.filtros import consulta_sem_cidade, consulta_com_cidade, normalize_path_params


# parametros para filtros personalizados
path_params = reqparse.RequestParser()
path_params.add_argument('city', type=str)
path_params.add_argument('star_min', type=float)
path_params.add_argument('star_max', type=float)
path_params.add_argument('daily_min', type=float)
path_params.add_argument('daily_max', type=float)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)


class Hoteis(Resource):
    def get(self):

        connection = sqlite3.connect('db_hotel.db')
        cursor = connection.cursor()

        dados = path_params.parse_args()
        dados_validos = {chave: dados[chave] for chave in dados if dados[chave] is not None}
        parametros = normalize_path_params(**dados_validos)

        if not parametros.get('city'):
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_sem_cidade, tupla)

        else:
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_com_cidade, tupla)

        hoteis = []
        for linha in resultado:
            hoteis.append({
                'hotel_id': linha[0],
                'nome': linha[1],
                'star': linha[2],
                'daily': linha[3],
                'city': linha[4],
                'site_id': linha[5]
            })

        return {"hoteis": hoteis}


class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name', type=str, required=True, help="Nome é obrigatório.")
    argumentos.add_argument('star', type=float, required=True, help="Informe as estrelas")
    argumentos.add_argument('daily', type=float, required=True, help="Diária não pode ficar em branco.")
    argumentos.add_argument('city', type=str, required=True, help="Local obrigatório.")
    argumentos.add_argument('site_id', type=int, required=True, help="Site obrigatório.")

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'mensagem': 'Hotel não encontrado.'}, 404

    @jwt_required
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': f'Hotel {hotel_id} já existe!'}

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)

        if not SiteModel.find_by_id(dados['site_id']):
            return {"message": "O Hotel precisa esta associado com um site_id válido."}, 400

        try:
            hotel.save_hotel()
        except:
            return {"message": "Erro ao salvar hotel."}, 500
        return hotel.json()

    @jwt_required
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            try:
                hotel_encontrado.save_hotel()
                return hotel_encontrado.json(), 200
            except:
                return {"message": "Erro ao salvar hotel."}, 500
        return {"message": "Hotel não encontrado."}, 404

    @jwt_required
    def delete(self, hotel_id):
        hotel_encontrado = HotelModel.find_hotel(hotel_id=hotel_id)
        if hotel_encontrado:
            try:
                hotel_encontrado.delete_hotel()
                return {"message": "Hotel deletedo."}
            except:
                return {"message": "Erro ao deletar hotel."}, 500
        return {"message": "Hotel não encontrado."}, 404

