import random

def get_random_temp(season):
    if 1<= season <=3:
        return round(random.uniform(-10,16), 1)
    elif 4<=season <=6:
        return round(random.uniform(16,23), 1)
    elif 7<=season <=9:
        return round(random.uniform(23,32), 1)
    else:
        return round(random.uniform(32,41), 1)
print(f"Test function: {get_random_temp(2)}")

def main():
    season = int(input("Please enter a number of month: "))
    random_temperture = get_random_temp(season)
    print(f"The temperature right now is {random_temperture} degrees Celsius.")
    if random_temperture<0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0<= random_temperture <=15.9:
        print("Quite chilly! Don’t forget your coat")
    elif 16<= random_temperture <=23.9:
        print("It's getting hotter,but you might still need a sweater")
    elif 24<= random_temperture <=32.9:
        print("The temperture is perfect!")
    else:
        print("It's hot outside! don't forget your water bottle")
main()