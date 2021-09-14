# with open('GIT\Week 10\Day 3\secrets.txt','r') as f:
#     print(f.read())

# with open('GIT\Week 10\Day 3\secrets.txt','r') as f:
#     files = f.readlines()
#     print(files[4])
#     for i in range(5):
#         print(files[i])
#     files = f.read().splitlines()
#     print(files.count('Lea'))


with open('GIT\Week 10\Day 3\secrets.txt','r+') as f:
    files = f.read().splitlines()
    # f.write('\nofer')
    for i in range(len(files)):
        if files[0] == 'Luke':
            files.insert(i,'SkyWalker')
    f.seek(0)
    f.write('\n'.join(files))