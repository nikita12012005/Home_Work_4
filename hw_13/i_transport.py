from abc import ABC, abstractmethod

class ITransport(ABC):

    @abstractmethod
    def start_engine(self): ...

    @abstractmethod
    def move(self, direction: str, distance: int): ...

    @abstractmethod
    def stop_engine(self): ...

