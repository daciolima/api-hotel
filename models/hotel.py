class HotelModel:
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
