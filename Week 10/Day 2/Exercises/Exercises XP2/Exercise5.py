def how_old():
    age_seconds = int(input("How old are you in seconds? "))
    earth_years = age_seconds/31557600
    print(f"you are {earth_years} Earth-years old.")
    print(f"you are {earth_years/0.2408467} Mercury-years old.")
    print(f"you are {earth_years/0.61519726} Venus-years old.")
    print(f"you are {earth_years/1.8808158} Mars-years old.")
    print(f"you are {earth_years/11.862615} Jupiter-years old.")
    print(f"you are {earth_years/29.447498} Saturn-years old.")
    print(f"you are {earth_years/84.016846} Uranus-years old.")
    print(f"you are {earth_years/164.79132} Neptune-years old.")
    
how_old()