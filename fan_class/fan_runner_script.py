from fan import Fan

fan_one = Fan(Fan.FAST, True, 10, "yellow")
fan_two = Fan(Fan.MEDIUM)

print(f"Fan One: {fan_one.get_speed()}, {fan_one.get_on()}, {fan_one.get_radius()}, {fan_one.get_color()}")
print(f"Fan Two: {fan_two.get_speed()}, {fan_two.get_on()}, {fan_two.get_radius()}, {fan_two.get_color()}")