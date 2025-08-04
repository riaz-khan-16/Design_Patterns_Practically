# Flyweight class (shared state)
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        print(f"Drawing {self.name} tree of color {self.color} at ({x}, {y})")

# Flyweight Factory to reuse TreeType objects
class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]

# Tree object with extrinsic state
class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        # Pass the unique state to the shared TreeType
        self.tree_type.draw(self.x, self.y)

# Client code: creating many trees
forest = []

# Adding 3 Pine trees at different locations
pine_type = TreeFactory.get_tree_type("Pine", "Green", "Rough")
forest.append(Tree(10, 20, pine_type))
forest.append(Tree(15, 25, pine_type))
forest.append(Tree(20, 30, pine_type))

# Adding 2 Oak trees at different locations
oak_type = TreeFactory.get_tree_type("Oak", "Dark Green", "Smooth")
forest.append(Tree(5, 10, oak_type))
forest.append(Tree(7, 14, oak_type))

# Drawing all trees
for tree in forest:
    tree.draw()
