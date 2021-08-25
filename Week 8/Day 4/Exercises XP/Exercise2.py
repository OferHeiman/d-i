class Dog():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return (self.weight/self.age*10)
    
    def fight(self,other_dog):
        if self.run_speed()*self.weight>other_dog.run_speed()*other_dog.weight:
            return f"{self.name} won the fight"
        elif self.run_speed()*self.weight<other_dog.run_speed()*other_dog.weight:
            return f"{other_dog.name} won the fight"
        else:
            return "The fight ended in a tie"

dog1 = Dog('Atlas',5,30)
dog2 = Dog('Helios',10,35)
dog3 = Dog('Icarus',2,20)
print(dog1.fight(dog2))
print(dog1.fight(dog3))
print(dog2.fight(dog3))