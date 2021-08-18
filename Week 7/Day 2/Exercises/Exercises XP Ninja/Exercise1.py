def box_printer(*args):
    longest_word = ''
    for i in range(len(args)):
        if len(args[i])>len(longest_word):
            longest_word = args[i]
    print("*"*(len(longest_word) + 4))
    for i in range(len(args)):
        print("* " + args[i] + (" "*(len(longest_word) - len(args[i]))) + " *")
    print("*"*(len(longest_word) + 4))
box_printer("Hello", "World", "in", "reallylongword", "a", "frame")