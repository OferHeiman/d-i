class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sphynx(Cat):
    pass

Generic_cat = Cat('Lily',10)
Bengal_cat = Bengal('Kitty',5)
Chartreux_cat = Chartreux('Bella',3)
Sphynx_cat = Sphynx('Cleo',13)
my_cats = [Generic_cat,Bengal_cat,Chartreux_cat,Sphynx_cat]
my_pets = Pets(my_cats)
my_pets.walk()