from random import randrange
def same_number(user_number: int):
    computer_number = randrange(1,101)
    if user_number == computer_number:
        print("Success")
    else:
        print("Fail",f"\nUser number:{user_number}",f"\nComputer number:{computer_number}")

user_number = int(input("Please enter a number between 1 and 100: "))
while True:
    if 1<= user_number <= 100:
        break
    user_number = int(input("Your number isn't valid,Please enter a number between 1 and 100: "))
    
same_number(user_number)