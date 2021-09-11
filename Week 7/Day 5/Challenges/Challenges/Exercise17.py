def weird_print(list1):
    weird_list = []
    for i in range(len(list1)):
        if i%2 == 0 and list1[i]%2 == 0:
            weird_list.append(i)
    print(weird_list)
weird_print([1,2,2,3,4,5])
