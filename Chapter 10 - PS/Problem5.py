# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.


class Train:
    def __init__(self, name, total_seats, fare):
        self.name = name
        self.total_seats = total_seats
        self.fare = fare

    def book_ticket(self):
        if self.total_seats > 0:
            self.total_seats -= 1
            print("Ticket booked successfully!")
        else:
            print("No seats available!")

    def get_status(self):
        print(f"Number of seats available: {self.total_seats}")

    def get_fare_info(self):
        print(f"Fare for the train {self.name}: {self.fare}")


# Example usage
train1 = Train("Rajdhani Express", 100, 1500)
train1.get_status()
train1.get_fare_info()
train1.book_ticket()
