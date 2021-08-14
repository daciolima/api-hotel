from sql_alchemy import db


class HotelModel(db.Model):

    __tablename__ = 'hoteis'
    hotel_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    star = db.Column(db.Float(precision=1))
    daily = db.Column(db.Float(precision=2))
    city = db.Column(db.String(80))

    def __init__(self, hotel_id, name, star, daily, city):
        self.hotel_id = hotel_id
        self.name = name
        self.star = star
        self.daily = daily
        self.city = city

    def json(self):
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "star": self.star,
            "daily": self.daily,
            "city": self.city
        }

    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel
        return None

    @classmethod
    def hotel_all(cls):
        hoteis = cls.query.all()
        if hoteis:
            return hoteis
        return None

    def update_hotel(self, name, star, daily, city):
        self.name = name
        self.star = star
        self.daily = daily
        self.city = city

    def save_hotel(self):
        db.session.add(self)
        db.session.commit()

    def delete_hotel(self):
        db.session.delete(self)
        db.session.commit()