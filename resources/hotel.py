from flask_restful import Resource


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

    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'messagem': 'Hotel não encontrado'}, 404

    def post(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
