from Exercise1 import Family

class TheIncredibles(Family):
    def __init__(self,last_name: str):
        self.last_name = last_name
        self.members = [{'name':'Robert','age':40,'gender':'Male','is_child':False,'power':'Superhuman Strength','incredible_name':'Mr.Incredible'},
       {'name':'Helen','age':38,'gender':'Female','is_child':False,'power':'Elasticity','incredible_name':'Elastigirl'},
       {'name':'Violet','age':14,'gender':'Female','is_child':True,'power':'Invisibility,Force Fields','incredible_name':'V'},
       {'name':'Dashiell','age':10,'gender':'Male','is_child':True,'power':'Super speed','incredible_name':'Dash'},]
    
    def use_power(self):
        for familymember in self.members:
            if familymember['age']>=18:
                print(familymember['name'])
            raise Exception(f"{familymember['name']} is not over 18")
    
    
    def incredible_presentation(self):
        for familymember in self.members:
            print(f"Incredible name: {familymember['incredible_name']}\nPower: {familymember['power']}\n")

family1 = TheIncredibles('Parr')
print("Family members:")
family1.print_members()
print("\nIncredible family members:")
family1.incredible_presentation()
family1.born(name = 'Jack',age = '1',gender = 'Male',is_child = True,power = 'Unknown Power',incredible_name = 'Jack Jack')
print("Family members:")
family1.print_members()
print("\nIncredible family members:")
family1.incredible_presentation()