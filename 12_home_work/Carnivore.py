from TerrestrialMammal import TerrestrialMammal

class Carnivore(TerrestrialMammal):
    def __init__(self, name, age, fur_color, habitat):
        super().__init__(name, age, fur_color, habitat)

    def hunt(self):
        print(f"{self.name} is hunting for prey.")

    def sharp_teeth(self):
        print(f"{self.name} has sharp teeth for tearing meat.")
