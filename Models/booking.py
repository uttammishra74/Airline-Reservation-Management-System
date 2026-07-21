class Booking():
    def __init__(self, passenger, flight, seat, price, status):
        self.passenger = passenger
        self.flight = flight
        self.seat = seat 
        self.price = price
        self.status = status


    def display(self):
        print(f"Passenger : {self.passenger}")
        print(f"Flight : {self.flight}")
        print(f"Seat : {self.seat}")
        print(f"Price : {self.price}")
        print(f"Status : {self.status}")
