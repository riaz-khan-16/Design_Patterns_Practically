# Subsystems
class Adder:
    def add(self, a, b):
        return a + b

class Subtractor:
    def subtract(self, a, b):
        return a - b

class Multiplier:
    def multiply(self, a, b):
        return a * b

class Divider:
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

#Now, you create a Facade:

class Calculator:
    def __init__(self):
        self.adder = Adder()
        self.subtractor = Subtractor()
        self.multiplier = Multiplier()
        self.divider = Divider()

    def calculate(self, operation, a, b):
        if operation == "add":
            return self.adder.add(a, b)
        elif operation == "subtract":
            return self.subtractor.subtract(a, b)
        elif operation == "multiply":
            return self.multiplier.multiply(a, b)
        elif operation == "divide":
            return self.divider.divide(a, b)
        else:
            return "Invalid Operation"

# Client
calc = Calculator()
print(calc.calculate("add", 10, 5))       # 15
print(calc.calculate("multiply", 3, 4))   # 12
print(calc.calculate("divide", 10, 0))    # Cannot divide by zero
