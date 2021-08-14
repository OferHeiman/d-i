family = {}
while True:
    name_and_age=input("Please enter a name and an age with a space between them,type 'done' when you finished entering all the people:")
    if name_and_age == 'done':
        break
    name_and_age=name_and_age.split(" ")
    family[name_and_age[0]]=int(name_and_age[1])
# 3.How much does each family member have to pay ?
# rick - 15$,beth - 15$,morty - 10$,summer - 10$
total_price=0
for person in family:
    if family[person]>3 and family[person]<12:
        total_price+=10
    elif family[person]>=12:
        total_price+=15
print(f"The total price of you movies tickets are: {total_price}$")