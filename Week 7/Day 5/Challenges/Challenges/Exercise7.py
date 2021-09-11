def list_count(list1,char):
    count = 0
    for c in list1:
        if c == char:
            count +=1
    return count
print(list_count(['a','a','t','o'],'a'))