def is_mono(list1):
    if list1 == sorted(list1) or list1 == sorted(list1,reverse=True):
        return True
    return False
print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))