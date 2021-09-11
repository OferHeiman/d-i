def find_max(list1):
    max_num = list1[0]
    for num in list1:
        if num>max_num:
            max_num = num
    return max_num
list1 = [15,5,500,150]
print(find_max(list1))