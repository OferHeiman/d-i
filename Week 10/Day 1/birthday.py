import datetime
def birthday():
    x = datetime.datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
    y = datetime.datetime.now()
    print(f"My birthday is in {x-y}")

birthday()