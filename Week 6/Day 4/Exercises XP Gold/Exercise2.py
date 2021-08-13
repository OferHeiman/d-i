user_number1=int(input("Please type the first number: "))
user_number2=int(input("Please type the second number: "))
user_number3=int(input("Please type the third number: "))
if user_number1 >= user_number2 and user_number1 >= user_number3:
    print(f"The greatest number is: {user_number1}")
elif user_number2 >= user_number1 and user_number2 >= user_number3:
    print(f"The greatest number is: {user_number2}")
else:
    print(f"The greatest number is: {user_number3}")
