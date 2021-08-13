user_fruits=input("What are you favourite fruits?(separate the fruits with a single space) ")
list_fruits=list(user_fruits.split(' '))
user_name_fruit=input("Type a name of any fruit: ")
if user_name_fruit in list_fruits:
    print("You chose one of your favorite")
else:
    print("You chose a new fruit. I hope you enjoy")
    