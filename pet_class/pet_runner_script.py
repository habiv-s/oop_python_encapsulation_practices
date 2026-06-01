from pet import Pet

the_pet = Pet("", "", 0)

pet_name_input = input("\033[31mEnter a pet name:\033[0m ")
the_pet.set_name(pet_name_input)

pet_animal_type_input = input("\033[31mEnter your pet animal type:\033[0m ")
the_pet.set_animal_type(pet_animal_type_input)

pet_age_input = input("\033[31mEnter your pet age:\033[0m ")
the_pet.set_age(pet_age_input)

print(f"""
======================
   MEET YOUR PET!!!
\033[33m{the_pet.pet_image()}\033[m
======================
      \033[32mPET DATA\033[0m
======================
\033[33mName:\033[0m {the_pet.get_name()}
\033[33mType:\033[0m {the_pet.get_animal_type()}
\033[33mAge:\033[0m {the_pet.get_age()}
======================""")