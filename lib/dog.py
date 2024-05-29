#!/usr/bin/env python3


APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    def __init__(self, name="Doggo", breed="Pug"):
        self.name = name
        self.breed = breed

    def name(self):
        return self._name
    def set_name(self, name):
        if isinstance (name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    name = property(name, set_name)
    
    def breed(self):
        return self._breed
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    
    breed = property(breed, set_breed)

new_dog = Dog()

print(new_dog.name)
print(new_dog.breed)