import re

username = input("What is your name? ")
if re.search("[A-Z][a-z]+ [A-Z][a-z]+",username):
    print('Name is valid')
else:
    print("Name is not valid")