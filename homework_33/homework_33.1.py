class Employee:
    company = "ABC Company"

    @classmethod
    def set_company(cls, name):
        cls.company = name
        return name

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"Name: {self.name}\nPosition: {self.position}\nCompany: {self.company}"


employee1 = Employee("Tina", "Manager")
employee2 = Employee("Oleg", "Developer")

print(employee1.get_info())

Employee.set_company("XYZ Company")
print(employee2.get_info())