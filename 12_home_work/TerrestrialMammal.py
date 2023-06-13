from Mammal import Mammal

class TerrestrialMammal(Mammal):
    def __init__(self, name, age, fur_color, habitat):
        super().__init__(name, age, fur_color)
        self.habitat = habitat

    def walk(self):
        print(f"{self.name} is walking on land.")

    def burrow(self):
        print(f"{self.name} is burrowing underground.")
