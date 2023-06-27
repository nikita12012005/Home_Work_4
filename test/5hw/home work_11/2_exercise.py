class Worker:
    def __init__(self, name: str, age: int, position: str, department: str, salary: float):
        self.name = name
        self.age = age
        self.position = position
        self.department = department
        self.salary = salary

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def get_position(self) -> str:
        return self.position

    def get_department(self) -> str:
        return self.department

    def get_salary(self) -> float:
        return self.salary

    def set_name(self, name: str):
        self.name = name

    def set_age(self, age: int):
        self.age = age

    def set_position(self, position: str):
        self.position = position

    def set_department(self, department: str):
        self.department = department

    def set_salary(self, salary: float):
        self.salary = salary

worker = Worker("John Smith", 30, "Software Engineer", "Engineering", 5000.00)


print(worker.get_name())
print(worker.get_age())
print(worker.get_position())
print(worker.get_department())
print(worker.get_salary())


worker.set_position("Senior Software Engineer")
worker.set_salary(6000.00)


print(worker.get_position())
print(worker.get_salary())

