class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high!")

davids_dog = Dog('Rex',50)
print(f"The dog's name is {davids_dog.name} and his height is {davids_dog.height}.")
davids_dog.bark()
davids_dog.jump()
sarahs_dog = Dog('Teacup',20)
print(f"The dog's name is {sarahs_dog.name} and his height is {sarahs_dog.height}.")
sarahs_dog.bark()
sarahs_dog.jump()
print(f"{davids_dog.name} is bigger") if davids_dog.height>sarahs_dog.height else print(f"{sarahs_dog.name} is bigger")