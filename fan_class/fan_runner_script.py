from fan import Fan

fan_one = Fan(Fan.FAST, True, 10, "yellow")
fan_two = Fan(Fan.MEDIUM)

print(f"""------------------
     FAN ONE
------------------
Speed: {fan_one.get_speed()}
Status: {fan_one.get_on()}
Radius: {fan_one.get_radius()}
Color: {fan_one.get_color()}
------------------""")

print("\n")

print(f"""------------------
     FAN TWO
------------------
Speed: {fan_two.get_speed()}
Status: {fan_two.get_on()}
Radies: {fan_two.get_radius()}
Color: {fan_two.get_color()}
------------------""")