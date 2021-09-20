import random
def get_words_from_file():
    word_list = open('GIT\Week 10\Day 4\Exercises\Exercises XP\sowpods.txt','r').read().splitlines()
    list_of_words = []
    for line in word_list:
        list_of_words.append(line)
    return list_of_words

def get_random_sentence(length):
    sentence = []
    for _ in range(length):
        sentence.append(random.choice(get_words_from_file()).lower())
    return ' '.join(sentence)

def main():
    print("The program creates a list of strings from a text file,and then creates a random sentence in the wanted length")
    while True:
        try:
            length = int(input("What length would you like the sentence to be between 2-20? "))
            if 2<=length<=20:
                break
            else:
                print("Length should be between 2-20")
        except:
            print("Your inputs data is incorrect,exiting program")
            return ""
    print(get_random_sentence(length))


main()