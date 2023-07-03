class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = "\n".join([f"  {key}: {value}" for key, value in self.__dict__.items()])
        return f"{class_name}:\n{attributes}"


car = Car("Tesla", "Model S", 2023)
print(car)
