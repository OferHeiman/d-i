class Farm():
    def __init__(self,name):
        self.name = name
        self.animals = {}
        print(f'{name}s farm')

    def add_animal(self,animal = '',amount = 1):
        if animal in self.animals:
            self.animals[animal] += amount
        else:
            self.animals[animal] = amount

    def get_info(self):
        for animal, amount in self.animals.items():
            print(f'{animal} : {amount}')
        print('\n    E-I-E-I-0!')
    
    def get_animal_types(self):
        return sorted(list(self.animals))
    def get_short_info(self):
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
