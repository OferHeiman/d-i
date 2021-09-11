list1 = ['hello',10,5,'how',300,'are','you',50]
integers_list = []
strings_list = []
for item in list1:
    if isinstance(item,int):
        integers_list.append(item)
    elif isinstance(item,str):
        strings_list.append(item)
print(integers_list)
print(strings_list)
