# Association, Aggregation, and Composition
# File name: association_aggregation_compostion.py

# 1. Association
# Two objects are related but can exist independently.
class Student:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Student: {self.name}")


class Laptop:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"Laptop Brand: {self.brand}")


# A student may have a laptop, but the laptop can exist without the student.
class StudentLaptopAssociation:
    def __init__(self, student, laptop=None):
        self.student = student
        self.laptop = laptop

    def display_info(self):
        self.student.display_info()
        if self.laptop:
            self.laptop.display_info()
        else:
            print("No laptop assigned.")


# 2. Aggregation
# Whole-part relationship where the part can exist separately.
class Teacher:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, name, teachers=None):
        self.name = name
        self.teachers = teachers if teachers is not None else []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def display_teachers(self):
        print(f"Department: {self.name}")
        for teacher in self.teachers:
            print(f"- Teacher: {teacher.name}")


# 3. Composition
# The whole owns the lifecycle of the part.
class Engine:
    def __init__(self, power):
        self.power = power


class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)  # Car owns Engine; Engine cannot exist separately in this case

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Engine Power: {self.engine.power} hp")


# Demo
student = Student("John Doe")
laptop = Laptop("Dell")
assoc = StudentLaptopAssociation(student, laptop)
assoc.display_info()

print("\n--- Aggregation ---")
teacher1 = Teacher("Alice")
teacher2 = Teacher("Bob")
department = Department("Computer Science", [teacher1, teacher2])
department.display_teachers()

print("\n--- Composition ---")
car = Car("Toyota", 180)
car.display_info()



# Aggregation: Has a Relationship
# A university has many departments, but departments can exist independently of the university.

class Department:
    def __init__(self, name):
        self.name = name
class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def display_departments(self):
        print(f"University: {self.name}")
        for department in self.departments:
            print(f"- Department: {department.name}")


un1 = University("ABC University")
dept1 = Department("Computer Science")
un1.add_department(dept1)
un1.display_departments()


#Composition
# A house has a room, and the room cannot exist without the house.
class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)

    def show_details(self):
        print(f"{self.brand} has an engine with {self.engine.power}HP")

car = Car( 'Toyota', 100)
car.show_details()

