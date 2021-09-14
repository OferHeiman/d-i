import datetime
def alive():
    x = datetime.datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
    y = datetime.datetime.now()
    print(f"The user has been alive for {y-x}")

alive()