from anagram_checker import AnagramChecker

def is_user_input_valid():
    while True:
        user_word = input("Input a word or type 'exit' to exit the program: ")
        if user_word.isalpha(): 
            return user_word

def anagram(): 
    print("Welcome to Anagram Checker!")
    user_word = is_user_input_valid()
    if user_word.lower() == 'exit':
        print('Exiting the program')
        return " "
    print(f"Your Word: {user_word}")
    print("This is a valid English word.")
    word_list = open('GIT\Week 10\Day 5\Exercises\Anagram Checker\sowpods.txt','r').read().splitlines()
    anagram = AnagramChecker(word_list)
    print(f"Anagrams for your word: {anagram.get_anagrams(user_word)}")

anagram()