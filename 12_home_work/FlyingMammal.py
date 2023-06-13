from Mammal import Mammal

class FlyingMammal(Mammal):
    def __init__(self, name, age, fur_color, wing_span):
        super().__init__(name, age, fur_color)
        self.wing_span = wing_span

    def fly(self):
        print(f"{self.name} is flying through the air.")

    def build_nest(self):
        print(f"{self.name} is building a nest.")
