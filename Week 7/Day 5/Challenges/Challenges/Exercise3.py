string = "Example Text"
print("Uppercase Letters: ", sum(1 for char in string if char.isupper()))
print("Lowercase Letters: ", sum(1 for char in string if char.islower()))