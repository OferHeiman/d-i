import random
class Dog():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"

class PetDog(Dog):
    def __init__(self, name, age, weight,trained = False):
        self.trained = trained
        super().__init__(name, age, weight)

    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self,*args):
        print(f"{','.join(list(args))} all play together")
    
    def do_a_trick(self):
        trick_list = [f'{self.name} does a barrel roll',f'{self.name} stands on his back legs',f'{self.name} shakes your hand',f'{self.name} plays dead']
        print(random.choice(trick_list)) if self.trained else print('The dog is not trained')

dog1 = PetDog('Triton',5,25)
dog1.train()
print(dog1.play('Abraxas','Castor','Eros'))
dog1.do_a_trick()