user_string = input("Please type a 10 characters long string ") #1
user_string_length = len(user_string)
while not user_string_length == 10:
    print("String not long enough.") if user_string_length < 10 else print("String too long.")
    user_string = input("Please type a 10 characters long string ")
    user_string_length = len(user_string)
    
print(user_string[0]+user_string[user_string_length-1]) #2

word_construction = "" #3
for i in user_string:
    word_construction += i
    print(word_construction)

import random
print(''.join(random.sample(user_string,user_string_length)))