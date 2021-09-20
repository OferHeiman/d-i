class Creature:
    id = 0
    def __init__(self,weight:int,ate_food:int) -> None:
        self.weight = weight
        self.ate_food = ate_food
        self.id = Creature.id
        Creature.id += 1
    
    
    def find_nearest_food(self, grid):
        pass


    def next_move(self, grid):
        pass
    

class World:
    def __init__(self,grid = [[]]) -> None:
        self.grid = grid
    

    def next_generation(self):
        pass


    def run(self):
        pass
        

world1 = World()