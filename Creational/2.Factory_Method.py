class Add:
  def __init__(self,a,b):
         self.a=a
         self.b=b
         print("Calculation result: ", self.a+self.b)

class Subtract:
     def __init__(self,a,b):
         self.a=a
         self.b=b
         print("Calculation result: ", self.a-self.b)
class Multiply:
     def __init__(self,a,b):
         self.a=a
         self.b=b
         print("Calculation result: ", self.a*self.b)


def calculate(input, a,b):
     if input=='add':
          return Add(a,b)
     if input=='subtract':
          return Subtract(a,b)
     if input=='multiply':
          return Multiply(a,b)

     
calculate('multiply',5,6)