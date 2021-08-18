s = input("String: ")
ch = input("Character: ")
count_char = 0
for char in s:
  if ch == char:
    count_char+=1
print(count_char)