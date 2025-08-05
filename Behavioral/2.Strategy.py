#Task: Go to work using different transport options.
#Step 1: Define the strategy interface

class TravelStrategy:
    def travel(self):
        pass
#Step 2: Create concrete strategies

class CarStrategy(TravelStrategy):
    def travel(self):
        print("Traveling by Car")

class BikeStrategy(TravelStrategy):
    def travel(self):
        print("Traveling by Bike")

class WalkStrategy(TravelStrategy):
    def travel(self):
        print("Walking to destination")

#Step 3: Context class that uses a strategy

class Navigator:
    def __init__(self, strategy: TravelStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: TravelStrategy):
        self.strategy = strategy

    def go_to_work(self):
        self.strategy.travel()
#Step 4: Use it
# Start with Car
nav = Navigator(CarStrategy())
nav.go_to_work()  # Traveling by Car

# Change to Bike
nav.set_strategy(BikeStrategy())
nav.go_to_work()  # Traveling by Bike

# Change to Walk
nav.set_strategy(WalkStrategy())
nav.go_to_work()  # Walking to destination