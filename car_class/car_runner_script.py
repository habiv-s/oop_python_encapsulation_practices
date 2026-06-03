from car import Car

car = Car(2026, "Aston Martin Valkyrie")
print(f"\033[93mMy car is {car._Car__year_model} {car._Car__make}.\033[0m")
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

print("\033[92mACCELERATING...\033[0m")
print("-" * 60)
for i in range(1, 6):
    car.accelerate()
    print(f"""\033[92mAcceleration {i} - Current Speed: {car.get_speed()} mph\033[0m
Hybrid State: {car.ers_deployment()}
Aero Wing: {car.active_aero()}""")
    print("-" * 60)

print("\n")

print("\033[91mBRAKING...\033[0m")
print("-" * 60)
for i in range(1, 6):
    car.brake()
    print(f"""\033[91mBrake {i} - Current Speed: {car.get_speed()} mph\033[0m
Hybrid State: {car.ers_deployment()}
Aero Wing: {car.active_aero()}""")
    print("-" * 60)
