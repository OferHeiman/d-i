import datetime
def Jan1st():
    x = datetime.datetime(2022,1,1)
    y = datetime.datetime.now()
    print(f"the 1st of January is in {x-y}")

Jan1st()