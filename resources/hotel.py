from flask_restful import Resource, reqparse


hoteis = [
    {'hotel_id': 560,
     'name': 'Plaza Hotel',
     'star': 4.3,
     'diaria': 450.00,
     'cidade': 'João Pessoa-PB'
     },
    {'hotel_id': 561,
     'name': 'Chica Hotel',
     'star': 4.0,
     'diaria': 420.00,
     'cidade': 'Fortaleza-CE'
     },
    {'hotel_id': 562,
     'name': 'Drummont Hotel',
     'star': 4.7,
     'diaria': 400.00,
     'cidade': 'Rio de Janeiro-RJ'
     },
    {'hotel_id': 563,
     'name': 'Praia Hotel',
     'star': 4.2,
     'diaria': 4220.00,
     'cidade': 'Recife-PE'
     },
    {'hotel_id': 564,
     'name': 'Sol e Mar',
     'star': 4.3,
     'diaria': 400.00,
     'cidade': 'João Pessoa-PB'
     },
    {'hotel_id': 565,
     'name': 'Sol Nascente',
     'star': 4.4,
     'diaria': 450.00,
     'cidade': 'Rio Grande do Norte-RN'
     }
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name')
    argumentos.add_argument('star')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    @staticmethod
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'mensagem': 'Hotel não encontrado.'}, 404

    def post(self, hotel_id):

        dados = Hotel.argumentos.parse_args()

        novo_hotel = {
            'hotel_id': hotel_id,
            'name': dados['name'],
            'star': dados['star'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }

        hoteis.append(novo_hotel)

        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()

        novo_hotel = {'hotel_id': hotel_id, **dados}  # linha enxuta

        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201


    def delete(self):
        pass
