class Wagon:
    def __init__(self, number):
        self._number = number
        self._passengers = []

    def add_passenger(self, passenger):
        if len(self._passengers) < 10:
            self._passengers.append(passenger)
        else:
            print("Wagon is full. Cannot add more passengers.")

    def __len__(self):
        return len(self._passengers)

    def __str__(self):
        return f"Wagon {self._number}: {len(self._passengers)} passengers"


class Train:
    def __init__(self):
        self.wagons = []

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        wagons_repr = "-".join(map(str, self.wagons[::-1]))
        return f"<=[HEAD]-{wagons_repr}"


train = Train()

wagon1 = Wagon(1)
wagon2 = Wagon(2)
wagon3 = Wagon(3)

wagon1.add_passenger("Passenger 1")
wagon1.add_passenger("Passenger 2")

wagon2.add_passenger("Passenger 3")

train.add_wagon(wagon1)
train.add_wagon(wagon2)
train.add_wagon(wagon3)

print(len(wagon1))
print(len(train))
print(train)
