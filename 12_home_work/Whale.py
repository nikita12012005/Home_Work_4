from MarineMammal import MarineMammal

class Whale(MarineMammal):
    def __init__(self, name, age, fur_color, swim_speed):
        super().__init__(name, age, fur_color, swim_speed)

    def sing(self):
        print(f"{self.name} is singing beautiful songs.")

    def breach(self):
        print(f"{self.name} is breaching out of the water.")
