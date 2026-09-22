class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # by convention, we use a single underscore for intended private data

    def get_salary(self, password):
        # In a real-world scenario, you would implement proper authentication logic here
        if password == "secret":
            return self._salary
        raise ValueError("Invalid password")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value


ob1 = Employee("John Doe", 30000)
ob2 = Employee("Jane Smith", 40000)

ob1.salary = 35000
print(ob1.salary)
print(ob2.salary)
print(ob1.name)
print(ob2.name)
print(ob1.get_salary("secret"))