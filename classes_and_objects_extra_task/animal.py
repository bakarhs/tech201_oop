class Dog:

    def __init__(self, name, size, colour):
        self.name = name
        self.size = size
        self.colour = colour
        self.breed = "Unknown"
        self.date_of_birth = "Unknown"
        self.animal_kind = "Canine"

    def bark(self):
        return("Woof!")

    def get_name(self):
        return (self.name)

    def dog_years(self):
        return (self.date_of_birth * 7)

buster = Dog("Buster", "Big", "Brown")
print(buster.bark())
print(buster.get_name())
buster.date_of_birth = 3
print(buster.dog_years())



