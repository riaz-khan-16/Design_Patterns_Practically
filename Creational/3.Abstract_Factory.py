## Abstract Products (interface)
class Chair:
    def sit(self):
        pass

class Table:
    def dine(self):
        pass



#### Concrete Produccts

class Chair1(Chair):
    def __init__(self):
        print("Chair 1 Created!")
class Chair2(Chair):
    def __init__(self):
        print("Chair 2 Created!")


class Table1(Table):
    def __init__(self):
        print("Table 1 Created!")
class Table2(Table):
    def __init__(self):
        print("Table 2 Created!")


##  Abstract Fatory:

class Factory:
    def create_chair(self):
        pass
    def create_table(self):
        pass

### Concrete Factories:

class FactoryType1(Factory):
    def create_chair(self):
        Chair1()
    def create_table(self):
        Table1()

class FactoryType2(Factory):
    def create_chair(self):
        Chair2()
    def create_table(self):
        Table2()

### now write client code

def create(factory):
    factory.create_chair()
    factory.create_table()


## when user need ffurnitures of typee 1
factory=FactoryType1()
create(factory)
    

## when user need ffurnitures of typee 1
factory=FactoryType2()
create(factory)


    


