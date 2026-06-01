from pet import Pet

the_pet = Pet("", "", 0)

pet_name_input = input("Enter a pet name: ")
the_pet.set_name(pet_name_input)

pet_animal_type_input = input("Enter your pet animal type: ")
the_pet.set_animal_type(pet_animal_type_input)

pet_age_input = input("Enter your pet age: ")
the_pet.set_age(pet_age_input)

print(f"""PET DATA
Name: {the_pet.get_name()}
Type: {the_pet.get_animal_type()}
Age: {the_pet.get_age()}
""")