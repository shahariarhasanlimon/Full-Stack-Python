class School:
    school_name = "Ostad High School"  # class variable
    def __init__(self, student_name, student_age):
        self.student_name = student_name  # instance variable
        self.student_age = student_age  # instance variable


School.school_name = "Hridoy Sishu Niketon"  # Modifying class variable
sc1 = School("John", 15)
print(sc1.school_name, sc1.student_name, sc1.student_age)  # Accessing class variable
sc2 = School("Alice", 14)
print(sc2.school_name, sc2.student_name, sc2.student_age)  # Accessing class variable