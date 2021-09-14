import string
import random
import re

def create_password():
    length = int(input("How many characters do you want your password to be? between 6-30 characters: "))
    while not 6 <= length <= 30:
         length = int(input("Invalid input,How many characters do you want your password to be? between 6-30 characters: "))
    password_requirments = string.ascii_letters + string.digits +string.punctuation
    while True:
        password = ''.join(random.choice(password_requirments) for i in range(length))
        if re.search('\w',password) and re.search('\d',password) and re.search('\W',password):
            return password

print(f"Password: {create_password()}")