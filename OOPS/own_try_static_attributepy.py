

class Vechile:

    industry = "Transport"  ## Static attribute defined
    
    def __init__(self, type, brand, name, model):
        self.type = type
        self.brand = brand
        self.name = name
        self.model = model
    
    def display_vechile(self):
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

v1 = Vechile("Car", "Toyota", "Etios", 2020)
v2 = Vechile("Bike", "Yamaha", "FZ-16", 2011)

v1.display_vechile()
v2.display_vechile()

v1.add_details("Yellow", "10KMPL")
v1.display_vechile()
v2.display_vechile()