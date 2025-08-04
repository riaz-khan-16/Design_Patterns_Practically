class Item:
    def get_count(self):
        pass

class Toy(Item):
    def __init__(self, name):
        self.name = name

    def get_count(self):
        return 1

class Box(Item):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item: Item):
        self.items.append(item)

    def get_count(self):
        return sum(item.get_count() for item in self.items)


# Create toys
toy1 = Toy("Toy 1")
toy2 = Toy("Toy 2")
toy3 = Toy("Toy 3")
toy4 = Toy("Toy 4")

# Create small box and add toys
small_box = Box("Small Box")
small_box.add(toy3)
small_box.add(toy4)

# Create big box and add toys + small box
big_box = Box("Big Box")
big_box.add(toy1)
big_box.add(toy2)
big_box.add(small_box)

print("Total toys in big box:", big_box.get_count())  # Output: 4
