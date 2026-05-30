class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, on=False, radius=5, color="blue"):
        self.__speed = int(speed)
        self.__on = bool(on)
        self.__radius = float(radius)
        self.__color = str(color)

    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.__speed = int(speed)

    def get_on(self):
        return self.__on
    def set_on(self, on):
        self.__on = bool(on)

    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        self.__radius = float(radius)

    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color