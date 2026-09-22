class School:
    school_name = "ABC School"  # Class variable

    @staticmethod
    def calculate_grade(marks):  # Static method
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        elif marks >= 60:
            return "D"
        else:
            return "F"

print(School.calculate_grade(85))  # Calling static method without creating an instance
    # @staticmethod
    # def display_school_name():
    #     print(f"School Name: {School.school_name}")
    # def __init__(self, student_name):
    #     self.student_name = student_name  # Instance variable