class Zoo():
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print('The animals in the zoo are:')
        for animal in self.animals:
            print(animal)

    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print('Sold the animal: '+animal_sold)

    def sort_animals(self):
        self.animals = sorted(self.animals)
        animals_dict = {}
        for animal in self.animals:
            for i in range(ord('A'),ord('Z')+1):
                if animal[0] == chr(i):
                    try:
                        animals_dict[chr(i)] += [animal]
                    except:
                        animals_dict[chr(i)] = [animal]
        return animals_dict
        
    def get_groups(self):
        animals = self.sort_animals()
        [print(f'{number} : {animal}') for number,animal in animals.items()]

zookeeper = Zoo('ramat_gan_safari')
zookeeper.add_animal('Ape')
zookeeper.add_animal('Bear')
zookeeper.add_animal('Alligator')
zookeeper.add_animal('Emu')
zookeeper.add_animal('Giraffe')
zookeeper.add_animal('Cheetah')
zookeeper.add_animal('Lion')
zookeeper.add_animal('Tiger')
zookeeper.add_animal('Goose')
zookeeper.add_animal('Leopard')
zookeeper.add_animal('Eagle')
zookeeper.add_animal('Tapir')
zookeeper.add_animal('Alpaca')
zookeeper.add_animal('Cougar')
zookeeper.add_animal('Baboon')
zookeeper.get_animals()
zookeeper.sell_animal('Ape')
print("Sorted the zoo:")
print(zookeeper.sort_animals())
print("These are the groups of animals:")
zookeeper.get_groups()
