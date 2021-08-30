class Family:
    def __init__(self,last_name: str):
        self.last_name = last_name
        self.members = [{'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}]
    
    def born(self,**kwargs):
        new_dict = {}
        for key,value in kwargs.items():
            new_dict[key]=value
        self.members.append(new_dict)
        print("Congratulations on your newborn!\n")
    

    def is_18(self,name):
        for familymember in self.members:
            return True if familymember['name'] == name and familymember['age']>=18 else False
    

    def print_members(self):
        for familymember in self.members:
            print(familymember['name'])

# family1 = Family('Berg')
# print(family1.members)
# family1.born(name = 'Walt', age = 0,gender = 'Male',is_child = True)
# print(family1.members)
# print(family1.is_18('Michael'))
# family1.print_members()