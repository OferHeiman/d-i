import re
def return_numbers(string):
    return ''.join(re.findall("\d",string))
print(return_numbers('k5k3q2g5z6x9bn'))