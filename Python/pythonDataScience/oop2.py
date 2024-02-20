class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Name = {self.name}, Email = {self.email}"


class Student(Person):
    def __init__(self, name, email, program):
        super().__init__(name, email)
        self.program = program

    def __str__(self):
        return f"{super().__str__()}, program = {self.program}"

    def result(self, marks):
        std_result = "Pass" if marks >= 50 else "Fail"
        print(std_result)


class Teacher(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    def __Str__(self):
        return f"{super().__str__()}, Salary= Rs.{self.salary}"

    def display_salary(self):
        print(f"Salary = Rs.{self.salary * 0.90}")
