"""line 6-7: i create a variable named x and give it an int value -5,using the built-in function abs() i get the absolute value and i print it.
line 9-10: i create a variable named future_integer and give it a string value "3",using the built-in function int() i convert the value to int and i print it.
line 13-14: i create a variable named my_input and and give it the built-in function input(),which lets the user type anything he wants,i think print the variable input.
line 17: i call this document explanation."""

x = -5
print(f"abs() result on {x}: {abs(x)}")

future_integer = "3"
print(f"int() result on {future_integer}: {int(future_integer)}")

my_input = input("Type anything you want: ")
print(f"input() result is: {my_input}")

print(__doc__)