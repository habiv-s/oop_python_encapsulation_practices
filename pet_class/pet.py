class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def pet_image(self):
        """Returns specific ASCII art based on the animal type attribute."""
        animal_type = self.__animal_type.strip().title()

        if animal_type == "Dog":
            return r"""
     __      _
    o'')}__// 
     `_/      )
     (_(_/-(_/
            """
        elif animal_type == "Cat":
            return r"""
          /\___/\  
         ( ^. .^ ) 
         ====v====
          (______)ﾉ
                    """
        elif animal_type == "Rabbit" or animal_type == "Bunny":
            return r"""
     (\ /)
     ( . .) 
    c(”)(”)
            """
        elif animal_type == "Fish":
            return r"""
     |\   /|
  ___| |_| |__
 /            \  ~ 
<   ( o ) ( o ) >  
 \____________/  ~ 
     | | | |
            """
        elif animal_type == "Hamster":
            return r"""
     (o___o)
    q( . . )p  
    (___Y___)
     ""   ""
            """
        elif animal_type == "Hedgehog":
            return r"""
     .|||||||..
    |||||||||||)
   < (  o . o )
     (  "  "  )
     `'-'--'-'`
            """
        else:
            return "No art available for this animal type."

    def status_bar(self):
        """Generates a visual health/happiness status bar for the terminal layout."""
        pass

    def speak(self):
        """Returns a stylized comic speech bubble with the pet's authentic sound."""
        pass