def longest_word(list1):
    long_word = list1[0]
    for word in list1:
        if len(word)>len(long_word):
            long_word = word
    return long_word

list1 = ['hello','how','are','you','doing']
print(longest_word(list1))