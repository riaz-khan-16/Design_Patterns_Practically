class Command:
       def execute(self):
            pass
       
##create receiver:
class Calculator:
       def add(self, a,b):
            print(a+b)
       def subtract(self, a, b):
           print(a-b)

#Create Commands
class addCommands(Command):
       def __init__(self, calculator, x, y):
              self.calculator=calculator
              self.x=x
              self.y=y
       def execute(self):
            self.calculator.add(self.x, self.y)
       
class SubtractCommands(Command):
       def __init__(self, calculator, x, y):
              self.calculator=calculator
              self.x=x
              self.y=y
       def execute(self):
            self.calculator.subtract(self.x, self.y)



###Create Invoker
class Invoker:
      def __init__(self):
            self.commands=[]
      def storeCommands(self,command):
            self.commands.append(command)
      def executeCommands(self):
            for command in self.commands:
                  command.execute()

#Client
calc=Calculator()
invoker=Invoker()
##Creating commands
invoker.storeCommands(addCommands(calc, 15,18))
invoker.storeCommands(SubtractCommands(calc, 5,2))
invoker.executeCommands()