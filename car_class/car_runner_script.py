from car import Car

Car = Car(2026, "Aston Martin Valkyrie")
print(f"My car is {Car._Car__year_model} {Car._Car__make}.")

print("ACCELERATING...")
Car.accelerate()
print(f"Current Speed: {Car.get_speed()}")

print("BRAKING...")
Car.brake()
print(f"Current Speed: {Car.get_speed()}")