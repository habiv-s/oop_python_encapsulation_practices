from car import Car

Car = Car(2026, "Aston Martin Valkyrie")
print(f"My car is {Car._Car__year_model} {Car._Car__make}.")

print("ACCELERATING...")
for i in range(5):
    Car.accelerate()
    print(f"Current Speed: {Car.get_speed()}")

print("BRAKING...")
for i in range(5):
    Car.brake()
    print(f"Current Speed: {Car.get_speed()}")