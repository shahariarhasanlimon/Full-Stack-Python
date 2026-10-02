# =============================
# 1. Single Inheritance
# =============================
class GrandFarther:
    # Parent class / Base class
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name

    def gf_method(self):
        print(f"GrandFather's color: {self.color}, First Name: {self.first_name}")


class Father(GrandFarther):
    # Single inheritance: Father inherits from GrandFarther
    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)  # Call parent constructor
        self.hobby = hobby

    def gf_method(self):
        # Method overriding: Father replaces the parent method with its own version
        print(f"Father's hobby: {self.hobby}, Color: {self.color}, First Name: {self.first_name}")


# =============================
# 2. Multilevel Inheritance
# =============================
class Children(Father):
    # Multilevel inheritance: Children -> Father -> GrandFarther
    def __init__(self, school, hobby, color, first_name):
        super().__init__(hobby, color, first_name)  # Father.__init__ calls GrandFarther.__init__
        self.school = school

    def child_method(self):
        print(f"School: {self.school}, Hobby: {self.hobby}, Color: {self.color}")


# =============================
# 3. Hierarchical Inheritance
# =============================
class Mother(GrandFarther):
    # Hierarchical inheritance: both Father and Mother inherit from GrandFarther
    def __init__(self, profession, color, first_name):
        super().__init__(color, first_name)
        self.profession = profession

    def mother_info(self):
        print(f"Mother's profession: {self.profession}, Color: {self.color}, Name: {self.first_name}")


# =============================
# 4. Multiple Inheritance
# =============================
class Teacher:
    # One parent class for multiple inheritance example
    def __init__(self, subject):
        self.subject = subject

    def teach(self):
        print(f"Teacher teaches: {self.subject}")


class Student:
    # Another parent class for multiple inheritance example
    def __init__(self, student_id):
        self.student_id = student_id

    def study(self):
        print(f"Student ID: {self.student_id}")


class SmartStudent(Student, Teacher):
    # Multiple inheritance: SmartStudent inherits from both Student and Teacher
    def __init__(self, student_id, subject, name):
        Student.__init__(self, student_id)
        Teacher.__init__(self, subject)
        self.name = name

    def show(self):
        print(f"Name: {self.name}, ID: {self.student_id}, Subject: {self.subject}")


# =============================
# 5. Hybrid Inheritance
# =============================
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Animal {self.name} speaks")


class Dog(Animal):
    # Hierarchical + multilevel type structure can be formed here
    def bark(self):
        print(f"{self.name} barks")


class Puppy(Dog):
    # Multilevel inheritance: Puppy -> Dog -> Animal
    def play(self):
        print(f"{self.name} is playing")


# =============================
# Run examples
# =============================
gf1 = GrandFarther("Red", "Chowdhury")
f1 = Father("Cricket", "Blue", "Rahim")
c1 = Children("Dhaka College", "Cricket", "Blue", "Rahim")
m1 = Mother("Teacher", "Black", "Amina")
s1 = SmartStudent("S-101", "Python", "Nabil")
p1 = Puppy("Milo")

print("1. Single Inheritance:")
gf1.gf_method()
print("\n2. Method override in Father:")
f1.gf_method()

print("\n3. Multilevel Inheritance:")
c1.gf_method()         # from Father
c1.child_method()      # from Children
print(c1.color)        # inherited from GrandFarther
print(c1.first_name)   # inherited from GrandFarther
print(c1.school)       # own attribute of Children
print(c1.hobby)        # inherited from Father

print("\n4. Hierarchical Inheritance:")
m1.mother_info()

print("\n5. Multiple Inheritance:")
s1.show()
s1.study()
s1.teach()

print("\n6. Hybrid / Combined Example:")
p1.speak()
p1.bark()
p1.play()

print("\nLearning note:")
print("Inheritance allows a class to reuse the properties and methods of another class.")
print("This reduces code repetition and makes programs more organized.")