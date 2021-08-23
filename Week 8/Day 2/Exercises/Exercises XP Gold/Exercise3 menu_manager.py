class MenuManager():
    menu = [
        {'name': 'Soup', 'price': 10, 'spice': 'B', 'gluten': False},
        {'name': 'Hamburger', 'price': 15, 'spice': 'A', 'gluten': True},
        {'name': 'Salad', 'price': 18, 'spice': 'A', 'gluten': False},
        {'name': 'French Fries', 'price': 5, 'spice': 'C', 'gluten': False},
        {'name': 'Beef bourguignon', 'price': 25, 'spice': 'B', 'gluten': True},
    ]

    def __init__(self):
        pass
    def add_item(self,name,price,spice,gluten):
        self.menu.append({'name':name,'price':price,'spice':spice,'gluten':gluten})
        print(f"{name} has been added to the menu: {self.menu[len(self.menu)-1]}")

    def update_item(self,name,price,spice,gluten):
        for dict in self.menu:
            if name == dict.get("name"):
                updated_dict = {'name':name,'price':price,'spice':spice,'gluten':gluten}
                dict.update(updated_dict)
                print(f"{name} has been updated: {dict} ")
                return   
        print(f"The dish {name} is not in the menu")

    def remove_item(self,name):
        for dict in self.menu:
            if name == dict.get("name"):
                self.menu.remove(dict)
                print(f"Removed {name} from the menu: \n{self.menu}")
                return   
        print(f"The dish {name} is not in the menu")

res = MenuManager()
res.add_item('Steak',30,'A',False)
res.update_item('Steak',35,'A',False)
res.remove_item('Salad')
