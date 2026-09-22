class Employee:
    company_name = "ABC Corporation"  # Class variable

    def __init__(self, employee_name, employee_id):
        self.employee_name = employee_name  # Instance variable
        self.employee_id = employee_id  # Instance variable

    def display_info(self): # instance method
        print(f"Employee Name: {self.employee_name}, Employee ID: {self.employee_id}")
        print(f"Company Name: {self.company_name}")  # Accessing class variable

    @classmethod
    def update_company_name(cls, new_name):  # class method
        cls.company_name = new_name

obj1 = Employee("John Doe", 101)
obj1.display_info()
obj1.update_company_name("XYZ Corporation")  # Changing class variable using class method
obj1.display_info()  # Displaying updated company name
print(Employee.company_name)  # Accessing class variable directly from the class

obj2 = Employee("Jane Smith", 102)
obj2.display_info()  # Displaying updated company name for the second object    
print(Employee.company_name)  # Accessing class variable directly from the class