class Employee:
    company_name = "ABC Corporation"  # Class variable

    def __init__(self, employee_name, employee_salary):
        self.employee_name = employee_name
        self._employee_salary = employee_salary

    @property
    def salary(self):
        return self._employee_salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._employee_salary = value

    def get_salary(self, password):
        if password == "secret":
            return self._employee_salary
        raise ValueError("Invalid password")

    def set_salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._employee_salary = value


ob1 = Employee("John Doe", 50000)
print(ob1.employee_name)
print(ob1.salary)
print(ob1.get_salary("secret"))

ob1.salary = 55000
print(ob1.salary)
print(ob1.get_salary("secret"))

ob1.set_salary(60000)
print(ob1.salary)
print(ob1.get_salary("secret"))