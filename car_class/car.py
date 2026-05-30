class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        pass

    def brake(self):
        pass

    def get_speed(self):
        return self.__speed