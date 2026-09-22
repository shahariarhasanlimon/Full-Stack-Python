#Car Class Banabo, Setar Kichu object banabo, jeta car er properties and methods ke represent korbe.
#Brand, Model 


# __init__() : Dunder method, Constructor
# Constructor 3 types 
# 1. Defualt Constructor
# 2. Parameterized Constructor 
# 3. Default Value Constructor 

# amra normally jake Function Boli, Seta k class er moddhe banale amra take method boli
class Car:
    def __init__(self, brand = "Honda", model = "Civic"):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

car1 = Car("Toyota", "Corolla")
print(car1.brand)
print(car1.model)

car2 = Car("Honda", "Civic")
print(car2.brand)
print(car2.model)

car1.display_info()
car2.display_info()