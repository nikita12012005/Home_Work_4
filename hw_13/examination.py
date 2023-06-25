from hw_13.car import Car

if __name__ == '__main__':
    car = Car()
    print(car.engine_status)
    car.start_engine()
    print(car.engine_status)
    print(car.get_coordinates())
    car.move("right", 5)
    print(car.get_coordinates())
    car.move("forward", 10)
    print(car.get_coordinates())

