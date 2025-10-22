class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Bark Bark !!")


class Owner:

    def __init__(self, ownername, address, contact):
        self.name = ownername
        self.address = address
        self.contact = contact

owner1 = Owner("Anu", "North road", 8823232)
dog1 = Dog("Tommy", "German Sheapard")
dog1.bark()
print(f"Dog1 Name : {dog1.name}")
print(f"Dog1 Breed :{dog1.breed}")
dog1.bark()
 
owner1 = Owner("Ban", "West road", 797797)
dog2 = Dog("Puppy", "Hussky")
dog2.bark()
print(f"Dog2 Name : {dog2.name}")
print(f"Dog2 Breed :{dog2.breed}")

