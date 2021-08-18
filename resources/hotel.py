from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required


class Hoteis(Resource):
    def get(self):
        hoteis_encontrados = HotelModel.hotel_all()
        if hoteis_encontrados:
            return {"hoteis": [hotel.json() for hotel in hoteis_encontrados]}
        return {"message": "Nenhum hotel cadastrado"}


class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name', type=str, required=True, help="Nome é obrigatório.")
    argumentos.add_argument('star', type=float, required=True, help="Informe as estrelas")
    argumentos.add_argument('daily', type=float, required=True, help="Diária não pode ficar em branco.")
    argumentos.add_argument('city', type=str, required=True, help="Local obrigatório.")

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

