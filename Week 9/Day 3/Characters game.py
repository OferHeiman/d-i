class Character():
    def __init__(self,name,life=20,attack=10) -> None:
        self.name = name
        self.life = life
        self.attack = attack
        print(f"You created a {self.__class__.__name__} Character named {self.name},with {self.life} life and {self.attack} attack.")
    

    def basic_attack(self,Character2):
        print(f"Before {self.name} basic attack's {Character2.name}, life: {Character2.life}")
        Character2.life -= self.attack
        print(f"After {self.name} basic attack's {Character2.name}, life: {Character2.life}")


class Druid(Character):
    def meditate(self):
        print(f"Before meditating: {self.name} life: {druid1.life} {self.name} attack: {druid1.attack}")
        self.life += 10
        self.attack -= 2
        print(f"After meditating: {self.name} life: {druid1.life} {self.name} attack: {druid1.attack}")
    

    def animal_help(self):
        print(f"Before animal_help: {self.name} attack: {druid1.attack}")
        self.attack += 5
        print(f"After animal_help: {self.name} attack: {druid1.attack}")
    

    def fight(self,Character2):
        print(f"{Character2.name} life before fight: {Character2.life}")
        Character2.life -= (0.75*self.life + 0.75*self.attack)
        print(f"{Character2.name} life after fight: {Character2.life}")


class Warrior(Character):
    def brawl(self,Character2):
        print(f"Before brawl: {Character2.name} life: {Character2.life}")
        print(f"Before brawl: {self.name} life: {self.life}")
        Character2.life -= (2*self.attack)
        self.life += (0.5*self.attack)
        print(f"After brawl: {Character2.name} life: {Character2.life}")
        print(f"After brawl: {self.name} life: {self.life}")
    

    def train(self):
        print(f"Before train: {self.name} life: {self.life} {self.name} attack: {self.attack}")
        self.attack += 2
        self.life +=2
        print(f"After train: {self.name} life: {self.life} {self.name} attack: {self.attack}")


    def roar(self,Character2):
        print(f"Before {self.name} roar's at {Character2.name}, attack: {Character2.attack}")
        Character2.attack -= 3
        print(f"After {self.name} roar's at {Character2.name}, attack: {Character2.attack}")
    

class Mage(Character):
    def curse(self,Character2):
        print(f"Before curse: {Character2.name} attack: {Character2.attack}")
        Character2.attack -= 2
        print(f"After curse: {Character2.name} attack: {Character2.attack}")
    

    def summon(self):
        print(f"Before summon: {self.name} attack: {self.attack}")
        self.attack += 3
        print(f"After summon: {self.name} attack: {self.attack}")
    

    def cast_spell(self,Character2):
        print(f"Before cast spell: {Character2.name} life: {Character2.life}")
        Character2.life -= (self.attack/self.life)


druid1 = Druid('Ballar',75,4)
warrior1 = Warrior('Ares',100,5)
mage1 = Mage('Hecubah',50,10)
druid1.meditate()
druid1.animal_help()
druid1.fight(warrior1)
warrior1.brawl(mage1)
warrior1.train()
warrior1.roar(druid1)
mage1.curse(warrior1)
mage1.summon()
mage1.basic_attack(warrior1)