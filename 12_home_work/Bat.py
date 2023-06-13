from FlyingMammal import FlyingMammal

class Bat(FlyingMammal):
    def __init__(self, name, age, fur_color, wing_span):
        super().__init__(name, age, fur_color, wing_span)

    def echolocation(self):
        print(f"{self.name} is using echolocation to navigate.")

    def hang(self):
        print(f"{self.name} is hanging upside down.")
