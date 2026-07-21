class Flight:
    def __init__(self, flight_number, source_airport, destination_airport, departure_time, arrival_time, economy_price, business_price, total_seats, available_seats, flight_id, status):
        self.flight_number = flight_number
        self.flight_id = flight_id
        self.source_airport = source_airport
        self.destination_airport = destination_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.economy_price = economy_price
        self.business_price = business_price
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.status = status

    def display(self):
        print(f"Flight No.  : {self.flight_number}")
        print(f"Flight id.  : {self.flight_id}")
        print(f"Source Airport : {self.source_airport}")
        print(f"Destination Airport : {self.destination_airport}")
        print(f"Departure Time : {self.departure_time}")
        print(f"Arrival Time : {self.arrival_time}")
        print(f"Economy Price : ${self.economy_price}")
        print(f"Business Price : ${self.business_price}")
        print(f"Total Seats : {self.total_seats}")
        print(f"Available Seats : {self.available_seats}")
        print(f"Status : {self.status}")