class GrandFarther:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name

class Father (GrandFarther):
    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)
        self.hobby = hobby

gf1 = GrandFarther("Red", "Chowdhury")
f1 = Father('Cricket', "Blue", "Rahim")
print(f1.color)  # This will raise an AttributeError because 'color' is not defined in Father class 
print(f1.first_name)  # This will also raise an AttributeError because 'first_name' is not defined in Father class