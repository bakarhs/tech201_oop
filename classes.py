# OOP -Object Oriented Programing

# Everything in OOP and objects are modelled against real world objects

# Classes are templates we use to create objects
# Classes are a way of bringing both data and functionality of our code together

# Create a class

class Dog:

    animal_kind = "Canine" # class variable
    animal_kind2 = "Octopus"

    def bark(self): # method
        return "Woof"

# self - "I'm referring to the current class".

#print(Dog.animal_kind)
#print(Dog.bark())

# Instantiation of a class

fido = Dog()
lassie = Dog()

print(type(fido))
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark())

Dog.animal_kind = "Dolphin" # Instance variable

print(fido.animal_kind) # Now outputs Dolphin
print(lassie.animal_kind) #Now outputs as Dolphin
print(lassie.animal_kind2) #Now outputs as Octopus

# The Dog's can still access their method
print(fido.bark())
print(lassie.bark())




