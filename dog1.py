# Initialisation

# Initialisation - Relates to setting a particular data for an instance of a class
# Instantiation - is the creation of an instance of an object

class Dog:

    def __init__(self, name, colour):
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour
        self.bark()

    def bark(self):
        return "woof"

# __init__

fido = Dog("Fido", "Brown")
lassie = Dog("Lassie", "Brown")

print(fido.name)
print(fido.colour)
print(lassie.bark())

# Initialising a class with class variables is good practice. It is possible to set a variable, but it is not advised




