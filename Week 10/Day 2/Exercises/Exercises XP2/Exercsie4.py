import datetime
def date_today():
    today_date = datetime.datetime.today()
    print(today_date)
    next_holiday = datetime.datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
    print(f"the next holiday is in {next_holiday-today_date}")

date_today()