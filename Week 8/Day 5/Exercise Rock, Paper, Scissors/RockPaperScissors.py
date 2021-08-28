from game import Game

def get_user_menu_choice():
    choice = input('''Menu:
    (g)Play a new game
    (s)Show scores
    (q)Quit
    Type here: ''')
    while True:
         if choice not in ('g','s','q'):
            choice = input('''Invalid input,Menu:
            (g)Play a new game
            (s)Show scores
            (q)Quit
            Type here: ''')
         else:
                return choice


def print_results(results):
    print(f'''
    Game Results:
     You won {results['win']} times
     You lost {results['lost']} times
     You drew {results['drew']} times
     ''')


def main():
    won = 0
    lost = 0
    drew = 0
    while True:
         results = {"win": won,"lost": lost,"drew": drew}
         menu = get_user_menu_choice()
         if menu == 'q':
            return 'Thank you for playing!'
         elif menu == 's':
             print_results(results)
         else:
             game = Game()
             user_item = game.get_user_item()
             computer_item = game.get_computer_item()
             result = game.get_game_result(user_item,computer_item)
             print(f"You chose: {user_item}, The computer chose: {computer_item}.\nthe result is: {result}")
             if result == 'win':
                 won += 1
             elif result == 'draw':
                 drew += 1
             else:
                 lost += 1

print(main())