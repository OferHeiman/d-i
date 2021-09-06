list_of_tuples = []
for i in range(5):
    name = input("name: ")
    age = input("age: ")
    score = input("score: ")
    my_tuple = (name,age,score)
    list_of_tuples.append(my_tuple)
print(f"Before sorting:\n{list_of_tuples}")
# list_of_tuples = [("Tom",19,80),("John",20,90),("Jony",17,91),("Jony",17,93),("Json",21,85)]
# print(list_of_tuples)
list_of_tuples.sort(key = lambda x: (x[0],x[1],x[2]))
print(f"After sorting:\n{list_of_tuples}")

