
class OldPrinter:
      def oldPrint(self, message):
            print(message)

class newPrinter:
      def print_message(self,message):
           print(message)

obj=newPrinter().print_message("Hi")
# obj=OldPrinter().print_message("Hi") #will raise error
class Adapter:
      def __init__(self,old_printer):
          self.old_printer=old_printer
      def print_message(self, message):
          self.old_printer.oldPrint(message)

old=OldPrinter()     
obj=Adapter(old)
obj.print_message("Hi") #now it will work