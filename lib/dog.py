#!/usr/bin/env python3

class Dog:
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

    def __init__(self, name, breed):
        self._name = None
        self._breed = None
        self.name = name
        self.breed = breed

    
    def get_name(self):
        return self._name

    def get_breed(self):
        return self._breed

    
    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    def set_breed(self, value):
        if value in Dog.APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")

    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


dog1 = Dog("Fido", "Corgi")
print(dog1.name)
print(dog1.breed)
