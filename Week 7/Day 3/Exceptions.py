my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
def sum():
    sum = 0
    for item in my_list:
        try:
            sum += item
        except:
            continue
    print(sum)
sum()