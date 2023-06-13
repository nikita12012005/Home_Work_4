from AquaticMammal import AquaticMammal

class MarineMammal(AquaticMammal):
    def __init__(self, name, age, fur_color, swim_speed):
        super().__init__(name, age, fur_color, swim_speed)

    def communicate(self):
        print(f"{self.name} is communicating underwater.")

    def feed(self):
        print(f"{self.name} is feeding on fish.")
