list_magicians = ["David Copperfield","David Blaine","Harry Houdini","Penn Jillette","Raymond Joseph Teller"]
def show_magicians(list_magicians):
    for i in range(len(list_magicians)):
        print(list_magicians[i])
def make_great():
    for i in range(len(list_magicians)):
        list_magicians[i]="The Great " + list_magicians[i]
make_great()
show_magicians(list_magicians)