user_words = input("Please enter 7 words with a space between each one: ")
words = user_words.split(' ')
letter = input("Please enter a single character: ")
for word in words:
    if letter in word:
            print(words.index(word))
    else:
        print(f"The letter {letter} isn't in the word {word}")