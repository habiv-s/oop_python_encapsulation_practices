class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    def get_speed(self):
        return self.__speed

    def ers_deployment(self):
        """Simulates the Valkyrie's F1-style Energy Recovery System (ERS)
           hybrid battery output based on your acceleration speed."""
        if self.__speed == 0:
            return "ERS - Idle [0 kW]"
        elif self.__speed < 15:
            return "ERS - Charging... [+40 kW]"
        else:
            return "ERS - Deploying Kinetic Boost! [-120 kW]"

    def active_aero(self):
        """Mimics Adrian Newey's active aerodynamics. The Valkyrie's
           wings adjust dynamically depending on how fast you loop it."""
        if self.__speed == 0:
            return "REAR WING - STOWED (0° Alpha)"
        elif self.__speed <= 15:
            return "ACTIVE AERO - LOW DRAG MODE"
        else:
            return "ACTIVE AERO - HIGH DOWNFORCE MODE [VENTURI OPEN]"