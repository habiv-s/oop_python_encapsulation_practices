from car import Car

Car = Car(2026, "Aston Martin Valkyrie")
print(f"\033[93mMy car is {Car._Car__year_model} {Car._Car__make}.\033[0m")
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
    Car.accelerate()
    print(f"""\033[92mAcceleration {i} - Current Speed: {Car.get_speed()} mph\033[0m
Hybrid State: {Car.ers_deployment()}
Aero Wing: {Car.active_aero()}""")
    print("-" * 60)

print("\n")

print("\033[91mBRAKING...\033[0m")
for i in range(1, 6):
    Car.brake()
    print(f"""\033[91mBrake {i} - Current Speed: {Car.get_speed()} mph\033[0m
Hybrid State: {Car.ers_deployment()}
Aero Wing: {Car.active_aero()}""")
    print("-" * 60)
