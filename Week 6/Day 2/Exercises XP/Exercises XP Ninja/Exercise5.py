longest_sentence = 0
while True: #Exercise asked for an infinite loop
    user_sentence = input("Type the longest sentence you can without the letter 'A' ")
    if 'A' not in user_sentence and len(user_sentence)>longest_sentence:
        print("Congratulations")
        longest_sentence = len(user_sentence)