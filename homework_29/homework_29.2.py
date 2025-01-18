class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Имя студента: {self.name}. Возраст студента: {self.age}"

students = [
Student("Oliver Smith", 18),
Student("Olivia Murphy", 20),
Student("Jessica Brown", 17),
Student("Sophie Roberts", 21),
Student("Oscar Taylor", 18),
Student("Thomas Miller", 19),
Student("William Johnson", 20),
Student("Alexander Li", 19),
Student("Mary Anderson", 22),
Student("Emma Morton", 18),
]

for student in students:
    print(student.display_info())