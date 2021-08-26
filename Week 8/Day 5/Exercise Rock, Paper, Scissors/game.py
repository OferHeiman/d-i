import random

class Game:
    def get_user_item(self):
        item = input("select rock\paper\scissors: ")
        while True:
            if item not in ('rock','paper','scissors'):
                item = input("Invalid input,Please type rock\paper\scissors: ") 
            else:
                return item
    
    def get_computer_item(self):
        computer_item = random.choice(['rock','paper','scissors'])
        return computer_item
    
    def get_game_result(self, user_item,computer_item):
        #user item is rock
        if user_item == 'rock' and computer_item == 'rock':
            return "draw"
        elif user_item == 'rock' and computer_item == 'paper':
            return "lose"
        elif user_item == 'rock' and computer_item == 'scissors':
            return "win"
        #user item is paper
        elif user_item == 'paper' and computer_item == 'paper':
            return "draw"
        elif user_item == 'paper' and computer_item == 'scissors':
            return "lose"
        elif user_item == 'paper' and computer_item == 'rock':
            return "win"
        #user item is scissors
        elif user_item == 'scissors' and computer_item == 'scissors':
            return "draw"
        elif user_item == 'scissors' and computer_item == 'rock':
            return "lose"
        elif user_item == 'scissors' and computer_item == 'paper':
            return "win"