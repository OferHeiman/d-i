my_list = [2, 24, 12, 354, 233] #list of integers
for i in range(len(my_list) - 1): # loops through the index of the list by using the length of the list,first time: i=0
    minimum = i #minimum=0 first time
    for j in range( i + 1, len(my_list)): # j=1 , range(1,5) first time,
        if(my_list[j] < my_list[minimum]): # 24 < 2 = False first time,
            minimum = j # doesnt go in first time,
            if(minimum != i): # doesnt go in first time,
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] # doesnt go in first time,
print(my_list)

my_list = [2, 24, 12, 354, 233]
my_list[0], my_list[1] = my_list[1], my_list[0]
print(my_list)
