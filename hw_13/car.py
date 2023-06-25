from hw_13.i_flyable import IFlyable
from hw_13.i_transport import ITransport


class Car(IFlyable, ITransport):

    def __init__(self):
        self.__engine_status= False
        self._brand= 'Chevrolet'
        self._model= 'Camaro'
        self._year_of_issue= 2016
        self._color= 'grey'
        self._speed= 0
        self._number_of_doors= 2
        self._fuel_consumption= 0
        self.__x = 0
        self.__y = 0
        self.__z = 0
        self._stands_still= True


    def start_engine(self):
        self.__engine_status= True

    def move(self, direction: str, distance: int):
        if direction == "right":
            self.__x += distance
        elif direction == "left":
            self.__x -= distance
        elif direction == "forward":
            self.__y += distance
        elif direction == "back":
            self.__y -= distance
        else:
            pass

    def stop_engine(self):
        self.__engine_status= False
        if not self._stands_still:
            self.braking()

    def fuel_consumption(self):
        self._fuel_consumption= 2

    def set_speed(self):
        self._speed= 70

    def braking(self):
        pass

    @property
    def engine_status(self):
        return self.__engine_status

    def get_coordinates(self) -> tuple:
        return self.__x, self.__y