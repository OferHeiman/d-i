names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("What is your name? ")
if user_name in names:
    print(names.index(user_name))
