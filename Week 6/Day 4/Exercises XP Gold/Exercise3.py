alphabet_string="abcdefghijklmnopqrstuvwxyz"
for letter in alphabet_string:
    if letter in ('a', 'e', 'i', 'o', 'u'):
	    print(f"{letter} is a vowel.")
    elif letter == 'y':
	    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
    else:
	    print(f"{letter} is a consonant.") 