class Airport:
    def __init__(self, airport_id, airport_name, airport_code, city, country):
        self.airport_id = airport_id
        self.airport_name = airport_name
        self.airport_code = airport_code
        self.city = city
        self.country = country

    def display(self):
        print(f"Airport ID   : {self.airport_id}")
        print(f"Airport Name : {self.airport_name}")
        print(f"Airport Code : {self.airport_code}")
        print(f"City         : {self.city}")
        print(f"Country      : {self.country}")