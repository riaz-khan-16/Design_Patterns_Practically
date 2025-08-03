#it is the main product: Calculator
class Calculator:
    def __init__(self):
        self.operations={}
    def add_operation(self,name,func):
        self.operations[name]=func
    def calculate(self, name, a, b):
        if name in self.operations:
            return self.operations[name](a,b)


# Build differennt parts of object

class CalculatorBuilder():
    def __init__(self):
        self.calculator = Calculator()

    def with_addition(self):
        self.calculator.add_operation("add", lambda a, b: a + b)
        return self

    def with_subtraction(self):
        self.calculator.add_operation("subtract", lambda a, b: a - b)
        return self

    def with_multiplication(self):
        self.calculator.add_operation("multiply", lambda a, b: a * b)
        return self

    def with_division(self):
        self.calculator.add_operation("divide", lambda a, b: a / b if b != 0 else "Cannot divide by zero")
        return self

    def build(self):
        return self.calculator
    

### build
#it is the main product: Calculator
class Calculator:
    def __init__(self):
        self.operations={}
    def add_operation(self,name,func):
        self.operations[name]=func
    def calculate(self, name, a, b):
        if name in self.operations:
            return self.operations[name](a,b)


# Build differennt parts of object

class CalculatorBuilder():
    def __init__(self):
        self.calculator = Calculator()

    def with_addition(self):
        self.calculator.add_operation("add", lambda a, b: a + b)
        return self

    def with_subtraction(self):
        self.calculator.add_operation("subtract", lambda a, b: a - b)
        return self

    def with_multiplication(self):
        self.calculator.add_operation("multiply", lambda a, b: a * b)
        return self

    def with_division(self):
        self.calculator.add_operation("divide", lambda a, b: a / b if b != 0 else "Cannot divide by zero")
        return self

    def build(self):
        return self.calculator
    

### build

builder=CalculatorBuilder()
my_calculator=builder.with_addition().with_subtraction().with_division().build() ## we are using add, sub, div and will not use multipliccation

ans=my_calculator.calculate('divide', 5, 5)



print(ans)





