from sql_alchemy import db


class HotelModel(db.Model):

    __tablename__ = 'hoteis'
    hotel_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    star = db.Column(db.Float(precision=1))
    daily = db.Column(db.Float(precision=2))
    city = db.Column(db.String(80))

    def __init__(self, hotel_id, name, star, diaria, cidade):
        self.hotel_id = hotel_id
        self.name = name
        self.star = star
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "star": self.star,
            "diaria": self.diaria,
            "cidade": self.cidade
        }
