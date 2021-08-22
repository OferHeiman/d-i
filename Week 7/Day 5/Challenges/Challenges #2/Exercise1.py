spaces = 2
for i in range(1,6,2):
    for j in range(0, spaces):  
        print(end=" ")
    spaces = spaces - 1 
    for j in range(0,i):  
        print("*", end="")       
    print()
print('------------------------------')  

spaces = 4
for i in range(5):
    for j in range(0, spaces):  
        print(end=" ")
    spaces = spaces - 1 
    for j in range(0,i+1):  
        print("*", end="")       
    print()
print('------------------------------')

for i in range(1,6):
    for j in range(0,i):  
        print("*", end="")       
    print()
spaces = 0
for i in range(5,-1,-1):
    for j in range(0,spaces):
        print(end=" ")
    spaces+=1
    for j in range(0,i):
        print("*", end="")       
    print()  