import random

def throw_dice():
    return random.randint(1,6)
def throw_until_doubles():
    count = 0
    dice1 = throw_dice()
    dice2 = throw_dice()
    while not dice1 == dice2:
        count+=1
        dice1 = throw_dice()
        dice2 = throw_dice()
    return count

def main():
    num_times_dices_thrown = 0
    for _ in range(100):
        num_times_dices_thrown += throw_until_doubles()
    print(f"Total throws:{num_times_dices_thrown}")
    print(f"Average throws to reach doubles:{num_times_dices_thrown/100}")
main()