from Mammal import Mammal

class AquaticMammal(Mammal):
    def __init__(self, name, age, fur_color, swim_speed):
        super().__init__(name, age, fur_color)
        self.swim_speed = swim_speed

    def swim(self):
        print(f"{self.name} is swimming in the water.")

    def dive(self):
        print(f"{self.name} is diving deep into the ocean.")
