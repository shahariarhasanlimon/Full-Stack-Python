class GrandFarther:
    # Base class: parent class
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name

    def gf_method(self):
        # Parent method
        print(f"GrandFather's color: {self.color}, First Name: {self.first_name}")


class Father(GrandFarther):
    # Child class inherits from GrandFarther
    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)  # Call parent constructor
        self.hobby = hobby  # New attribute of Father

    def gf_method(self):
        # This overrides the parent method
        print(f"Father's hobby: {self.hobby}, Color: {self.color}, First Name: {self.first_name}")


class Children(Father):
    # Grandchild class inherits from Father, and Father already inherits from GrandFarther
    def __init__(self, school, hobby, color, first_name):
        super().__init__(hobby, color, first_name)  # Calls Father.__init__ -> GrandFarther.__init__
        self.school = school  # New attribute of Children

    def child_method(self):
        # Child can use inherited attributes as well as its own
        print(f"School: {self.school}, Hobby: {self.hobby}, Color: {self.color}")


gf1 = GrandFarther("Red", "Chowdhury")
f1 = Father("Cricket", "Blue", "Rahim")
c1 = Children("Dhaka College", "Cricket", "Blue", "Rahim")

print("GrandFather object:")
gf1.gf_method()

print("\nFather object:")
f1.gf_method()  # Father method is called because it overrides parent method

print("\nChildren object:")
c1.gf_method()  # Python finds gf_method in Father first
c1.child_method()

print("\nInherited values:")
print(c1.color)      # inherited from GrandFarther
print(c1.first_name) # inherited from GrandFarther
print(c1.school)     # own attribute of Children
print(c1.hobby)      # inherited from Father