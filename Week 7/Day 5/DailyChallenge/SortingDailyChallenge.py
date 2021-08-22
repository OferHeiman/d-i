sequence_of_words = input("Type a comma separated sequence of words: ")
sequence_of_words = sequence_of_words.split(',')
sequence_of_words.sort()
print(','.join(sequence_of_words))