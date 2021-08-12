from flask_restful import Resource


hoteis = [
    {'hotel_id': 564,
     'name': 'Plaza Hotel',
     'star': 4.3,
     'diaria': 450.00,
     'cidade': 'João Pessoa-PB'
     },
    {'hotel_id': 565,
     'name': 'Chica Hotel',
     'star': 4.0,
     'diaria': 420.00,
     'cidade': 'Fortaleza-CE'
     },
    {'hotel_id': 566,
     'name': 'Drummont Hotel',
     'star': 4.7,
     'diaria': 400.00,
     'cidade': 'Rio de Janeiro-RJ'
     },
    {'hotel_id': 567,
     'name': 'Praia Hotel',
     'star': 4.2,
     'diaria': 4220.00,
     'cidade': 'Recife-PE'
     },
    {'hotel_id': 568,
     'name': 'Sol e Mar',
     'star': 4.3,
     'diaria': 400.00,
     'cidade': 'João Pessoa-PB'
     },
    {'hotel_id': 569,
     'name': 'Sol Nascente',
     'star': 4.4,
     'diaria': 450.00,
     'cidade': 'Rio Grande do Norte-RN'
     }
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
