class Passenger:
    def __init__(self, name, email, phone, password, date_joined):
        self.name = name
        self.email =  email
        self.phone = phone
        self.password = password
        self.date_joined = date_joined


    def display(self):
        print(f"Name : {self.name}")
        print(f"Email : {self.email}")
        print(int(f"Phone : {self.phone}"))
        print(f"Password : {self.password}")
        print(f"Date Joined : {self.date_joined}")