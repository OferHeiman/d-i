tuple_numbers = (1,2,3,4)
list_numbers=list(tuple_numbers)
list_numbers.append(5)
tuple_numbers=tuple(list_numbers)
print(tuple_numbers)

# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# You can't add more values to the tuple,but you can workaround it by creating a different mutable object like lists,and convert it back into a tuple.