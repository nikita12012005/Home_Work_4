from abc import ABC, abstractmethod

class ITraveling(ABC):


    @abstractmethod
    def set_speed(self):...

    @abstractmethod
    def fuel_consumption(self):...

    @abstractmethod
    def braking(self):...

