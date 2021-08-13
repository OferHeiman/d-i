# list_of_names=['ofer','itai','ayal','dan','liza','adisu','daniela','noa']
# new_list_of_names = []
# for i in range(0,len(list_of_names)):
#     age=int(input(f"What is your age {list_of_names[i]}? "))
#     if age>16:
#         new_list_of_names.append(list_of_names[i])
# print(new_list_of_names)

# list_of_names=['ofer','itai','ayal','dan','liza','adisu','daniela','noa']
# i=0
# while i<len(list_of_names):
#     age=int(input(f"What is your age {list_of_names[i]}? "))
#     if age<16:
#         list_of_names.pop(i)
#     else:
#         i+=1
# print(list_of_names)

list_of_names=['ofer','itai','ayal','dan','liza','adisu','daniela','noa']
for i in range(len(list_of_names)-1,-1,-1):
    age = int(input(f"What is your age {list_of_names[i]}? "))
    if age < 16:
        list_of_names.pop(i)
print(list_of_names)

