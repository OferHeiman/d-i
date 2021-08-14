encrypt_or_decrypt = input("Would you like to encrypt or decrypt? ")
text = input("Type your text: ")
cypher_text = ''
shift = int(input("How much would you like to shift? "))
for letter in text:
    cypher_text += chr(ord(letter) + shift)  
if encrypt_or_decrypt == 'encrypt':
    print("Your encrypted text is:\n"+cypher_text+"\nYour shift is:"+str(shift))
else:
    print("Your decrypted text is:\n"+cypher_text+"\nYour shift is:"+str(shift))