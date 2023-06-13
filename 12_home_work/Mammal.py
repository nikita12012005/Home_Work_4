from Animal import Animal

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"{self.name} is giving birth to live young.")

    def nurse(self):
        print(f"{self.name} is nursing its young.")
