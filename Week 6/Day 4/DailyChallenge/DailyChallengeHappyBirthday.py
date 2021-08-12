import datetime
user_birthday = input("What is your birthdate? use format DD/MM/YYYY: ")
user_birthday = user_birthday.replace('/', '')
# checks age
birth_date = datetime.date(int(user_birthday[4:8]), int(user_birthday[2:4]), int(user_birthday[0:2]))
today = datetime.date.today()
age = today.year - int(user_birthday[4:8]) - ((today.month, today.day) < (int(user_birthday[2:4]), int(user_birthday[0:2])))
# checks if leap year
is_leap_year = None
user_birthyear = int(user_birthday[4:8])
if (user_birthyear % 4) == 0:
    if (user_birthyear % 100) == 0:
        if (user_birthyear % 400) == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False
# prints cake
num_candles = age % 10
for i in range(is_leap_year+1):
    if num_candles == 0:
        print("    ___________")
    elif num_candles == 1:
        print("    _____", end="")
        for _ in range(num_candles):
            print("i", end="")
        print("_____")
    elif num_candles == 2:
        print("    ____", end="")
        for _ in range(num_candles):
            print("i", end="")
        print("_____")
    elif num_candles == 3:
        print("    ____", end="")
        for _ in range(num_candles):
            print("i", end="")
        print("____")
    elif num_candles == 4:
        print("    ___", end="")
        for _ in range(num_candles):
            print("i", end="")
        print("____")
    elif num_candles == 5:
        print("    ___", end="")
        for _ in range(num_candles):
            print("i", end="")
        print("___")
    elif num_candles == 6:
        print("    __", end="")
        for _ in range(num_candles):
            print("i", end="")
        print("___")
    elif num_candles == 7:
        print("    __", end="")
        for _ in range(num_candles):
            print("i", end="")
        print("__")
    elif num_candles == 8:
        print("    __", end="")
        for _ in range(num_candles):
            print("i", end="")
        print("_")
    elif num_candles == 9:
        print("    _", end="")
        for _ in range(num_candles):
            print("i", end="")
        print("_")
    print('''   |:H:a:p:p:y:|
 __|___________|__
|^^^^^^^^^^^^^^^^^|
|:B:i:r:t:h:d:a:y:|
|                 |
~~~~~~~~~~~~~~~~~~~''')
