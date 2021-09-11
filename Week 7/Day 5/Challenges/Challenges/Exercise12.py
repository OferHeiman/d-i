def is_palindrome(string):
    if string[0].capitalize() == string[len(string)-1].capitalize():
        return True
    return False
print(is_palindrome('Tenet'))
print(is_palindrome('John'))