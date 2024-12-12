class FormAddress:
    def __init__(self, city, street, house, floor=None):
        self.city = city
        self.street = street
        self.house = house
        self.floor = floor

    def __repr__(self):
        floor_info = f", Floor: {self.floor}" if self.floor else ""
        return f"Location: {self.street} {self.house}, {self.city}{floor_info}"

    def address_tuple(self):
        return (self.city, self.street, self.house, self.floor)