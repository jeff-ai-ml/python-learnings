

class Vechile:

    industry = "Transport"  ## Static attribute defined
    
    def __init__(self, type, brand, name, model):
        self.type = type
        self.brand = brand
        self.name = name
        self.model = model
    
    def display_vechile(self):
        print("Vechile General Details")
        print(f"Name of Vechile : {self.name}")
        print(f"Model of Vechile : {self.model}")
        print(f"Brand of Vechile : {self.brand}")
        print(f"Type of Vechile : {self.type}")
        print(f"Vechile Industry : {Vechile.industry}")   ## Static attribute used

        try:
            if self.color and self.millage:
                print(f"Type of Vechile : {self.color}")
                print(f"Type of Vechile : {self.millage}")
        except:
            None
        print("\n")
    
    def add_details(self,color,millage):
        self.color = color
        self.millage = millage        

class Car(Vechile):
    def __init__(self, type, brand, name, model,doors,wheels):
        super().__init__(type, brand, name, model)
        self.num_of_doors = doors
        self.num_of_wheels = wheels

    def display_doors_wheels(self):
        print("Vechile General Doors and Wheels")
        print(f"Number of Doors : {self.num_of_doors}")
        print(f"Number of Wheels : {self.num_of_wheels}")

class Bike(Vechile):
    def __init__(self, type, brand, name, model,doors,wheels):
        super().__init__(type, brand, name, model)
        self.num_of_doors = doors
        self.num_of_wheels = wheels
        print("Vechile General Doors and Wheels")
        print(f"Number of Doors : {self.num_of_doors}")
        print(f"Number of Wheels : {self.num_of_wheels}")


c1 = Car("Car", "Toyota", "Etios", 2022, 4, 5)
c1.display_vechile()
c1.display_doors_wheels()

b1 = Car("Bike", "Yamaha", "FZ16", 2022, 4, 5)
b1.display_vechile()
b1.display_doors_wheels()