class Payment:
    def __init__(self, payment_id, booking_id, amount, method, payment_status):
        self.payment_id = payment_id
        self.booking_id = booking_id
        self.amount = amount
        self.method = method
        self.payment_status = payment_status

    def display(self):
        print(f"Payment id: {self.payment_id}")
        print(f"Booking id: {self.booking_id}")
        print(f"Amount: {self.amount }")
        print(f"Method: {self.method}")
        print(f"Payment Status: {self.payment_status}")