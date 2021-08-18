def divide():
    try:
        result = 5/0
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
divide()