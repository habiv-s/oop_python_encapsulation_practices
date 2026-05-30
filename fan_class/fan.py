class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed, on, radius, color):
        self.__speed = int(speed)
        self.__on = bool(on)
        self.__radius = float(radius)
        self.__color = str(color)