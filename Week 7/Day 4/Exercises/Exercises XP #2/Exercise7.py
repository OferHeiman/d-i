def get_age(year, month, day):
    person_age = 2021 - year
    return person_age

def can_retire(gender, date_of_birth):
    date_of_birth = date_of_birth.split('/')
    date_of_birth = list(map(int,date_of_birth))
    age = get_age(date_of_birth[0],date_of_birth[1],date_of_birth[2])
    if gender == 'm' and age>=67:
        print("You can retire")
        return True
    elif gender == 'f' and age>=62:
        print("You can retire")
        return True
    else:
        print("You can't retire")
        return False
print(can_retire(input("What is your gender? type 'm' for male and 'f' for female: "),input("What is your date of birth? use format YYYY/MM/DD: ")))