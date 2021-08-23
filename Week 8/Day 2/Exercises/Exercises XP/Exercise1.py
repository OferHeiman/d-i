class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def find_oldest_cat(*args):
    oldest_cat = args[0]
    for cat in args:
        if cat.age>oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

Cat1 = Cat('Cleo',5)
Cat2 = Cat('Nala',3)
Cat3 = Cat('Albert',15)
oldest_cat = find_oldest_cat(Cat1,Cat2,Cat3)
print(f"The oldest cat is {oldest_cat.name}, and he is {oldest_cat.age} years old.")