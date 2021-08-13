family_ages = input("What are the ages of everyone who wants a ticket in the family?")
family_ages_list = list(map(int,family_ages.split(' ')))
total_price = 0
for i in range(0,len(family_ages_list)):
    if family_ages_list[i]>=3 and family_ages_list[i]<=12:
        total_price += 10
    elif family_ages_list[i]>12:
        total_price += 15
print(total_price)

list_permitted_teens= []
while True:
    user=input("What is your age?(Type 'quit' if there are no more teens) ")
    if user=='quit':
        break
    if int(user)>=16 and int(user)<=21:
        list_permitted_teens.append(user)
print(list_permitted_teens)