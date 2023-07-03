class Worker:
    def __init__(self, name: str, age: int, position: str, department: str, salary: float):
        self.__name = name
        self.__age = age
        self.__position = position
        self.__department = department
        self.__salary = salary

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @property
    def position(self) -> str:
        return self.__position

    @property
    def department(self) -> str:
        return self.__department

    @property
    def salary(self) -> float:
        return self.__salary

    @name.setter
    def name(self, name: str):
        self.__name = name

    @age.setter
    def age(self, age: int):
        self.__age = age

    @position.setter
    def position(self, position: str):
        self.__position = position

    @department.setter
    def department(self, department: str):
        self.__department = department

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary

    def promote(self):
        pass

    @staticmethod
    def calculate_bonus(salary: float) -> float:
        pass

    @classmethod
    def from_dict(cls, worker_dict):
        pass


if __name__ == "__main__":
    worker = Worker("John Smith", 30, "Software Engineer", "Engineering", 5000.00)

    print(worker.name)
    print(worker.age)
    print(worker.position)
    print(worker.department)
    print(worker.salary)

    worker.position = "Senior Software Engineer"
    worker.salary = 6000.00

    print(worker.position)
    print(worker.salary)
