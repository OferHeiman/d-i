class Human:
    def __init__(self,name:str,age:int,living_place = None) -> None:
        self.name = name
        self.age = age
        self.living_place = living_place 
    
    def move(self,Building):
        self.living_place = Building
        Building.inhabitants.append(self)


class Building:
    def __init__(self,address:str,inhabitants = []):
        self.address = address
        self.inhabitants = inhabitants 


class City:
    def __init__(self,name:str,buildings = []):
        self.name = name
        self.buildings = buildings 
    
    def construct(self,address):
        self.buildings.append(address)
    
    def info_city(self):
        citizens_combined_age = 0
        number_of_citizens = 0
        for building in self.buildings:
            for inhabitant in building.inhabitants:
                citizens_combined_age += inhabitant.age
                number_of_citizens +=1
        print(f"There are {len(self.buildings)} buildings in the city of {self.name}, and the median age of the citizens is {citizens_combined_age/number_of_citizens}.")


ofer = Human('Ofer',25)
roni = Human('Roni',34)
shalom = Human('Shalom',68)
itai = Human('Itai',25)
michael = Human('Michael',32)
building = Building('Hamagen 25')
building2 = Building('Ben gurion 11')
ofer.move(building)
roni.move(building)
itai.move(building)
shalom.move(building2)
michael.move(building2)
city = City('Gotham')
city.construct(building)
city.construct(building2)
city.info_city()