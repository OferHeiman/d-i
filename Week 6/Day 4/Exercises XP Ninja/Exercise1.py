import math
user_input = input('Type a comma separated string of numbers: ')
user_input = user_input.split(',')
for i in range(len(user_input)):
    user_input[i] = round(math.sqrt((2*50*int(user_input[i]))/30))
print(user_input)