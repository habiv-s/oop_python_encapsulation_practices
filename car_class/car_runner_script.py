from car import Car

Car = Car(2026, "Aston Martin Valkyrie")
print(f"My car is {Car._Car__year_model} {Car._Car__make}.")
print("\033[94m" + r"""                                  ____________________                       
                          ______//                   \\\______              
                     ____/      /  [ AM VALKYRIE ]    \       \____         
         ___________/          /                       \           \______  
       / ____                                                             \ 
 _____/_/    \______     _                             _     ______/\_____/
 \_             __  \   // \                          // \   /  __        / 
   |__    __   /  \  |  \\_/  ______________________  \\_/  |  /  \   ___|  
      \__/  \ | () | |_______/                      \_______| | () | /      
             \ \__/ /                                        \ \__/ /       
              \____/                                          \____/        """ + "\033[0m")

print("\n")

print("ACCELERATING...")
print("-" * 60)
for i in range(1, 6):
    Car.accelerate()
    print(f"""Acceleration {i} - Current Speed: {Car.get_speed()}
Hybrid State: {Car.ers_deployment()}
Aero Wing: {Car.active_aero()}""")
    print("-" * 60)

print("\n")

print("BRAKING...")
for i in range(1, 6):
    Car.brake()
    print(f"""Brake {i} - Current Speed: {Car.get_speed()}
Hybrid State: {Car.ers_deployment()}
Aero Wing: {Car.active_aero()}""")
    print("-" * 60)
