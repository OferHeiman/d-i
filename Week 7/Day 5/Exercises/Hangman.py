def body_parts(wrong_guesses):
    if wrong_guesses == 1:
        return '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
    elif wrong_guesses==2:
                return '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
    elif wrong_guesses==3:
        return '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
    elif wrong_guesses==4:
        return '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''
    elif wrong_guesses==5:
        return '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
    elif wrong_guesses==6:
        return '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
def Hangman(word):
    player_letter = ""
    list_of_player_letters = ""
    hangman_word = list('*'*len(word))
    wrong_guesses=0
    while wrong_guesses<6:
        player_letter = input("Please type a letter: ").lower()
        flag = True
        while flag:
            if (player_letter in list_of_player_letters) or (player_letter.isalpha() == False) or (len(player_letter)>1):
                player_letter = input(f"You either already guessed the letter {player_letter} or your letter is invalid,Please type in a letter: ")
            else:
                flag=False
        list_of_player_letters+=player_letter
        print("You tried the letters:" + list_of_player_letters)
        if player_letter in word:
            for x in range(len(word)):
                for n in range(len(list_of_player_letters)):
                    if word[x] == list_of_player_letters[n]:
                        hangman_word[x] = list_of_player_letters[n]
        else:
            wrong_guesses+=1
            print(body_parts(wrong_guesses))
        print(''.join(hangman_word))
        if '*' not in hangman_word:
            return print("You Win")
    return print("You Lose")
Hangman(word)
