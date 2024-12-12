import csv
from lxml import etree
from ClassFormAddress import FormAddress


class AddressBook:
    def __init__(self):
        self.locations = {}
        self.floor_distribution = {}

    def clear(self):
        self.locations.clear()
        self.floor_distribution.clear()

    def add_address(self, location):
        loc_tuple = location.address_tuple()
        if loc_tuple in self.locations:
            self.locations[loc_tuple]['count'] += 1
        else:
            self.locations[loc_tuple] = {'count': 1, 'floor_distribution': {}}

        if location.floor is not None:
            if location.floor not in self.locations[loc_tuple]['floor_distribution']:
                self.locations[loc_tuple]['floor_distribution'][location.floor] = 0
            self.locations[loc_tuple]['floor_distribution'][location.floor] += 1

    def read_from_csv(self, file_path):
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            header = next(reader)  # Пропускаем заголовок
            for row in reader:
                city = row[header.index("city")].strip('"')
                street = row[header.index("street")].strip('"')
                house = row[header.index("house")]
                floor = row[header.index("floor")] if "floor" in header else None
                location = FormAddress(city, street, house, floor)
                self.add_address(location)

    def read_from_xml(self, file_path):
        with open(file_path, 'rb') as file:
            doc = etree.parse(file)
        for item in doc.xpath("//item"):
            location = FormAddress(item.get("city"), item.get("street"), item.get("house"), item.get("floor"))
            self.add_address(location)

    def results(self):
        for (city, street, house, floor), info in self.locations.items():
            if info['count'] > 1:
                print(
                    f"Следующая запись: Город: {city}, Улица: {street}, Дом: {house}, Этаж: {floor} - имеет {info['count']} вхождений")

        print()
        city_floors = {}
        for (city, _, _, floor), info in self.locations.items():
            if city not in city_floors:
                city_floors[city] = {}
            if floor is not None:
                if floor not in city_floors[city]:
                    city_floors[city][floor] = 0
                city_floors[city][floor] += info['floor_distribution'].get(floor, 0)

        for city, floors in city_floors.items():
            print(f"{city}:")
            for floor, count in floors.items():
                print(f"{floor} - этажный: {count} домов")
            print()
