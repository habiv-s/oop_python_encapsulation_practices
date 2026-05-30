from fan import Fan

fan_one = Fan(Fan.SLOW, False, 67, "red")

print(f"Fan One: {fan_one.get_speed()}, {fan_one.get_on()}, {fan_one.get_radius()}, {fan_one.get_color()}")