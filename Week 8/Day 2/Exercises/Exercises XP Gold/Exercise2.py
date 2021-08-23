import random
class MyList():
    def __init__(self,list_of_letters):
        self.list_of_letters = list_of_letters
    
    def reverseSort(self):
        self.list_of_letters.reverse()
        return self.list_of_letters
    
    def sortList(self):
        list_of_letters = sorted(self.list_of_letters)
        return list_of_letters
    
    def generateSecondList(self):
        second_list = []
        [second_list.append(round(random.random()*100)) for x in range(len(self.list_of_letters))]
        return second_list
letters = MyList(['b','a','c'])
letters = letters.sortList()
print(letters)
letters = MyList(letters).reverseSort()
print(letters)
print(MyList(letters).generateSecondList())