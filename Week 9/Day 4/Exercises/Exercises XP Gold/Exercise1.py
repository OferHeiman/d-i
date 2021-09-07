class Door():
    objs = 0
    next = []
    keys = abs(int(input("How many keys do you have? ")))
    def __init__(self,locked:bool):
        Door.objs += 1
        self.locked = locked
        self.id = Door.objs
        self.next.append(self)
    
    def can_go_to(self,other_door):
        if self.id>other_door.id:
            for i in range(self.id-other_door.id+1):
                if Door.next[other_door.id+i-1].locked == True and Door.keys == 0:
                    return f"The path from door {self.id} to door {other_door.id} can't be made."
                elif Door.next[other_door.id+i-1].locked:
                    print(f"Opened door {Door.next[other_door.id+i-1].id}")
                    Door.keys = Door.keys - 1
        else:
            for i in range(other_door.id-self.id+1):
                print(f"Door id: {Door.next[self.id+i-1].id}, Locked: {Door.next[self.id+i-1].locked}")
                if Door.next[self.id+i-1].locked and Door.keys == 0:
                    return f"The path from door {self.id} to door {other_door.id} can't be made."
                elif Door.next[self.id+i-1].locked and Door.keys>0: 
                    print(f"Opened door {Door.next[self.id+i-1].id}")
                    Door.keys = Door.keys - 1
                    print(f"Keys left: {Door.keys}")
        return f"The path from door {self.id} to door {other_door.id} can be made."

door1 = Door(False)
door2 = Door(False)
door3 = Door(True)
door4 = Door(True)
door5 = Door(False)
door6 = Door(False)
print(door1.can_go_to(door6))