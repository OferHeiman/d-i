users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
disney_users_A= {}
disney_users_B= {}
disney_users_C= {}

for i in range(0,len(users)):
    disney_users_A[users[i]]=i
print(disney_users_A)

for i in range(0,len(users)):
    disney_users_B[i]=users[i]
print(disney_users_B)

users.sort()
for i in range(0,len(users)):
    disney_users_C[users[i]]=i
print(disney_users_C)

# Question 4 is unclear,do i need two new results or only one? i wrote both just in case
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.
disney_users_A.clear()
for i in range(0,len(users)):
    if 'i' in users[i] and (users[i][0]=='M' or users[i][0]=='P'):
        disney_users_A[users[i]]=i
print(disney_users_A)
# or maybe this is the what the question asked for
disney_users_A.clear()
for i in range(0,len(users)):
    if 'i' in users[i]:
        disney_users_A[users[i]]=i
print(disney_users_A)

users[i][0]=='M' or users[i][0]=='P'
disney_users_A.clear()
for i in range(0,len(users)):
    if users[i][0]=='M' or users[i][0]=='P':
        disney_users_A[users[i]]=i
print(disney_users_A)
