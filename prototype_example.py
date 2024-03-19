import copy

class Prototype:
    def __init__(self):
        self.data = []

    def clone(self):
        return copy.deepcopy(self)

# Create a prototype
prototype_instance = Prototype()

# Clone the prototype
clone_instance = prototype_instance.clone()