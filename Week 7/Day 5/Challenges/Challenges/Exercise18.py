def type_count(**kwargs):
    integers = 0
    strings = 0
    floats = 0
    bools = 0
    for key,value in kwargs.items():
        if isinstance(value,str):
            strings +=1
        elif isinstance(value,float):
            floats +=1
        elif isinstance(value,bool):
            bools +=1
        elif isinstance(value,int):
            integers +=1
    print(f"int: {integers},str: {strings},float: {floats},bool: {bools}")

type_count(a=1,b='string',c=1.0,d=True,e=False)