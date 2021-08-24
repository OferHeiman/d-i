from typing import List


class Farm():
    def __init__(self,name):
        self.name = name
        self.animals = {}
        print(f'{name}s farm')

    def add_animal(self,animal: str,amount: int = 1) -> None:
        self.animals[animal] = self.animals.get(animal, 0) + amount

    def get_info(self) -> None:
        [print(f'{animal} : {amount}') for animal,amount in self.animals.items()]
        print('\n    E-I-E-I-0!')
    
    def get_animal_types(self) -> List:
        return sorted(self.animals)

    def get_short_info(self) -> None:
        animal_list = macdonald.get_animal_types()   
        print(f"{self.name}'s farm has {animal_list[0]}s,{animal_list[1]}s and {animal_list[2]}.")


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
print(macdonald.get_animal_types())
macdonald.get_short_info()
