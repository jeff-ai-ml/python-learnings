class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Bark Bark !!")

dog1 = Dog("Tommy", "German Sheapard")
dog1.bark()
print(f"Dog1 Name : {dog1.name}")
print(f"Dog1 Breed :{dog1.breed}")
dog1.bark()
 

dog2 = Dog("Puppy", "Hussky")
dog2.bark()
print(f"Dog2 Name : {dog2.name}")
print(f"Dog2 Breed :{dog2.breed}")

