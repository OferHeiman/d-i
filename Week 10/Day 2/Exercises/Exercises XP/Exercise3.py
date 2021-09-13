import string    
import random 
word = ''.join(random.choices(string.ascii_letters, k=5))    
print(f"The randomly generated string is : {word}")