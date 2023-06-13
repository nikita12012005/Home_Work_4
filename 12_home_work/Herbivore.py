from TerrestrialMammal import TerrestrialMammal

class Herbivore(TerrestrialMammal):
    def __init__(self, name, age, fur_color, habitat):
        super().__init__(name, age, fur_color, habitat)

    def graze(self):
        print(f"{self.name} is grazing on vegetation.")

    def flat_teeth(self):
        print(f"{self.name} has flat teeth for grinding plants.")
