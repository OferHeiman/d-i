a = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] #1
for number in a: print(number,end=" ") #2.a
print("")
b = sorted(a,reverse=True)
for number in b: print(number,end=" ") #2.b
print("")
print(sum(a)) #2.c
print([a[0],a[len(a)-1]]) #3
greater_50 = []
for num in a:
    if num >50:
        greater_50.append(num)
print(greater_50) #4
smaller_10 = []
for num in a:
    if num <10:
        smaller_10.append(num)
print(smaller_10) #5
squard_list = []
for num in a: squard_list.append(num**2)
print(squard_list) #6
no_duplicates = []
for number in a:
    if not number in no_duplicates:
        no_duplicates.append(number)
print(f"There are {len(no_duplicates)} in the new list")
print(no_duplicates)#7
print(sum(a)/len(a))#8
largest_number = a[0]
for number in a:
    if number>largest_number:
        largest_number = number
print(largest_number)#9
smallest_number = a[0]
for number in a:
    if number<smallest_number:
       smallest_number = number
print(smallest_number)#10
