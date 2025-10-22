class Dog:

    def __init__(self, name, breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Bark Bark !!")


class Owner:

    def __init__(self, ownername, address, contact):
        self.name = ownername
        self.address = address
        self.contact = contact

owner1 = Owner("Anu", "North road", 8823232)
dog1 = Dog("Tommy", "German Sheapard", owner1)
dog1.bark()
print(f"Dog1 Name : {dog1.name}")
print(f"Dog1 Breed :{dog1.breed}")
print(f"Dog1 Owner details: {dog1.owner.name, dog1.owner.address, dog1.owner.contact}")
dog1.bark()
 
owner2 = Owner("Ban", "West road", 797797)
dog2 = Dog("Puppy", "Hussky", owner2)
dog2.bark()
print(f"Dog2 Name : {dog2.name}")
print(f"Dog2 Breed :{dog2.breed}")
print(f"Dog2 Owner details: {dog2.owner.name, dog2.owner.address, dog2.owner.contact}")

