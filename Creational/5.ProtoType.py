import copy

# Base Prototype class
class Calculator:
    def __init__(self, model,name):
        self.model = model
        self.name=name
    
    def clone(self):
        return copy.deepcopy(self)
    
obj=Calculator(100, "basic")
print(obj.name, obj.model)
obj2=obj.clone()
print(obj2.name, obj2.model)