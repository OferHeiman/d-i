import random

class Human:
    def __init__(self,id_number:str,name:str,age:int,priority:bool,blood_type:str):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self,person):
        self.family.append(person)
        person.family.append(self)
    
    def __repr__(self) -> str:
        return repr(f"Name: {self.name}, Age:{self.age}, Priority: {self.priority}")

class Queue:
    def __init__(self):
        self.humans = []
    
    def add_person(self, person):
        self.humans.insert(0,person) if person.age > 60 or person.priority else self.humans.append(person)
    
    def find_in_queue(self,person):
        return self.humans.index(person)
        #Ayal way to do it
        # for i in range(len(self.humans)):
        #     if self.humans[i].id_number == person.id_number:
        #         return i
        # return -1 #person doesn't exist in waiting list
    
    def swap(self,person1,person2):
        person1_index = self.find_in_queue(person1)
        person2_index = self.find_in_queue(person2)
        self.humans[person1_index] = person2
        self.humans[person2_index] = person1
        #Ayal way to do it
        # self.humans.pop(person1_index) 
        # self.humans.insert(person1_index,person2)
        # self.humans.pop(person2_index)
        # self.humans.insert(person2_index,person1)
    
    def get_next(self):
        try:
            person = self.humans[0]
            self.humans.pop(0)
            return person
        except:
            return None
    
    def get_next_blood_type(self,blood_type):
        for human in self.humans:
            if human.blood_type == blood_type: 
                self.humans.pop(self.find_in_queue(human)) 
                return human
        return None

    @staticmethod
    def age_func(human): #returns the age of the person
        return human.age

    def sort_by_age(self):
        priority = []
        no_priority = []
        for human in self.humans:
            if human.priority:
                priority.append(human)
            else:
                no_priority.append(human)
        priority.sort(key=self.age_func,reverse=True)
        no_priority.sort(key=self.age_func,reverse=True)
        self.humans = priority
        self.humans.extend(no_priority)

    def rearrange_queue(self):
            for i in range(len(self.humans)-1):
                if self.humans[i] in self.humans[i+1].family:
                    random.shuffle(self.humans)
                    i=0


human1 = Human("1",'ofer',25,False,'A')
human2 = Human("2",'guy',65,True,'AB')
human3 = Human("3",'tal',61,False,'O')
human4 = Human("4",'yuval',35,True,'B')
human5 = Human("5",'liam',35,False,'A')
human6 = Human("6",'emma',67,True,'AB')
human7 = Human("7",'noah',65,False,'O')
human8 = Human("8",'oliver',37,True,'B')
human9 = Human("9",'elijah',31,False,'A')
human10 = Human("10",'william',85,True,'AB')
human11 = Human("11",'james',71,False,'O')
human12 = Human("12",'ben',19,True,'B')
human13 = Human("13",'lucas',28,False,'A')
human14 = Human("14",'alex',95,True,'AB')
human15 = Human("15",'mia',79,False,'O')
human16 = Human("16",'harper',34,True,'B')
human1.add_family_member(human9)
human2.add_family_member(human14)
human3.add_family_member(human10)
human4.add_family_member(human16)
human5.add_family_member(human15)
human6.add_family_member(human11)
human7.add_family_member(human12)
human8.add_family_member(human13)
queue = Queue()
queue.add_person(human1)
queue.add_person(human2)
queue.add_person(human3)
queue.add_person(human4)
queue.add_person(human5)
queue.add_person(human6)
queue.add_person(human7)
queue.add_person(human8)
queue.add_person(human9)
queue.add_person(human10)
queue.add_person(human11)
queue.add_person(human12)
queue.add_person(human13)
queue.add_person(human14)
queue.add_person(human15)
queue.add_person(human16)
print("Queue:")
for human in queue.humans:
    print(f"ID number: {human.id_number}, Name: {human.name}, Age:{human.age}, Priority: {human.priority}, Blood type: {human.blood_type}, Family: {human.family}")
print("sorting by age and priority")
queue.sort_by_age()
for human in queue.humans:
     print(f"ID number: {human.id_number}, Name: {human.name}, Age:{human.age}, Priority: {human.priority}, Blood type: {human.blood_type}, Family: {human.family}")
print("Rearrange so no family members near each other in queue")
queue.rearrange_queue()
for human in queue.humans:
    print(f"ID number: {human.id_number}, Name: {human.name}, Age:{human.age}, Priority: {human.priority}, Blood type: {human.blood_type}, Family: {human.family}")