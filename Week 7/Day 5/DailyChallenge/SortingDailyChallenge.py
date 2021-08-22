sequence_of_words = input("Type a comma separated sequence of words: ")
word_list = sorted([word for word in sequence_of_words.split(',')])
print(','.join(word_list))