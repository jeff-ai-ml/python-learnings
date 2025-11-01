

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
        print(f"Road Tax : {Vechile.get_road_tax(self)}")    ## Static method used
        print(f"Vechile Industry : {Vechile.industry}")   

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

    @staticmethod                ## Static method defined
    def get_road_tax(self):
        if self.model <2010:
            return 1500
        else:
            return 5000
                

v1 = Vechile("Car", "Toyota", "Etios", 2020)
v2 = Vechile("Bike", "Yamaha", "FZ-16", 2011)

v1.display_vechile()
v2.display_vechile()
v1.add_details("Yellow", "10KMPL")
v1.display_vechile()
v2.display_vechile()