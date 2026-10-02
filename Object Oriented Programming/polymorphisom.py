# Poly = Multiple
# Morphism = Many Forms
# In simple words: one thing can behave in many ways.

# 1. Method Overriding
# Same method name in parent and child class, but child version runs.
class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name

    def gf_method(self):
        # Parent method
        print(f"GrandFather's color: {self.color}, First Name: {self.first_name}")


class Father(GrandFather):
    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)
        self.hobby = hobby

    def gf_method(self):
        # Child method overrides parent method
        print(f"Father's hobby: {self.hobby}, Color: {self.color}, First Name: {self.first_name}")


class Children(Father):
    def __init__(self, school, hobby, color, first_name):
        super().__init__(hobby, color, first_name)
        self.school = school

    def gf_method(self):
        # Again overriding: this child version will run instead of parent's version
        print(f"Child's school: {self.school}, Hobby: {self.hobby}, Name: {self.first_name}")


# 2. Method Overloading in Python (simulated)
# Python does not support method overloading like Java/C++ directly.
# But we can use default arguments or *args to give a method many forms.
class Calculator:
    def add(self, a, b=None, c=None):
        # This single method can work with 2 numbers or 3 numbers
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        else:
            return a + b + c


# 3. Operator Overloading
# Same operator (+, -, *, ==) behaves differently for different classes.
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        # + operator is overloaded to add page counts
        return self.pages + other.pages

    def __lt__(self, other):
        # < operator is overloaded to compare pages
        return self.pages < other.pages


# 4. Duck Typing Example
# If an object behaves like a duck, Python accepts it.
class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


# 5. Polymorphism with same method name on different classes
class Shape:
    def area(self):
        print("Area of shape is calculated")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Same method name, different behavior
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Another same-name method with different behavior
        return 3.14 * self.radius * self.radius


# =========================
# Example Run
# =========================
print("Method Overriding Example:")
g1 = GrandFather("Red", "Chowdhury")
f1 = Father("Cricket", "Blue", "Rahim")
c1 = Children("Dhaka College", "Cricket", "Blue", "Rahim")

g1.gf_method()  # GrandFather's method
f1.gf_method()  # Father's method overrides parent
c1.gf_method()  # Child's method overrides both parent versions

print("\nMethod Overloading Simulation:")
cal = Calculator()
print(cal.add(5))
print(cal.add(5, 10))
print(cal.add(5, 10, 15))

print("\nOperator Overloading:")
book1 = Book(200)
book2 = Book(350)
print(book1 + book2)  # uses __add__
print(book1 < book2)  # uses __lt__

print("\nDuck Typing:")
d = Dog()
c = Cat()
for animal in (d, c):
    animal.sound()  # same method name, different behavior

print("\nSame method name, different class implementations:")
rect = Rectangle(5, 4)
circle = Circle(3)
print("Rectangle area:", rect.area())
print("Circle area:", circle.area())

print("\nPolymorphism Summary:")
print("Polymorphism means one interface or method name can behave differently in different classes.")
print("This helps write cleaner and reusable code.")