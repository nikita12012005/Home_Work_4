class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


car = Car("Tesla", "Model S", 2023)


def print_object(car):
    class_name = car.__class__.__name__
    print(f"{class_name}:")
    for key, value in car.__dict__.items():
        print(f"  {key}: {value}")


print_object(car)
