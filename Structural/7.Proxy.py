class MovieTheater:
    def enter(self):
        print("Welcome to the movie theater!")

class TicketCheckerProxy:
    def __init__(self, has_ticket):
        self.has_ticket = has_ticket
        self.theater = MovieTheater()

    def enter(self):
        if self.has_ticket:
            self.theater.enter()
        else:
            print("You must buy a ticket to enter.")

# You don’t have a ticket
proxy1 = TicketCheckerProxy(False)
proxy1.enter()  # Output: You must buy a ticket to enter.

# You have a ticket
proxy2 = TicketCheckerProxy(True)
proxy2.enter()  # Output: Welcome to the movie theater!
