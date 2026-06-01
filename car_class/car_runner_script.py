from car import Car

my_car = Car(2026, "Aston Martin Valkyrie")
print(f"My car is {my_car._Car__year_model} {my_car._Car__make}.")

print("ACCELERATING...")
my_car.accelerate()
print(f"Current Speed: {my_car.get_speed()}")

print("BRAKING...")
my_car.brake()
print(f"Current Speed: {my_car.get_speed()}")