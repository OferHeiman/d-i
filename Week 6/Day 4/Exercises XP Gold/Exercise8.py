games_won_counter = 0
games_lost_counter = 0
while True:
    user_number = input("Please enter a number from 1-9(including),if you want to quit type 'quit': ")
    if user_number == 'quit':
        break
    else:
        import random
        random_number = random.randrange(9)+1
        if int(user_number) == random_number:
            print("Winner")
            games_won_counter += 1
        else:
            print("Better luck next time")
            games_lost_counter += 1
print(f'''Number of games won: {games_won_counter}
Number of games lost: {games_lost_counter}''')
