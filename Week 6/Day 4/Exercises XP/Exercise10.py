total_price= 10
while True:
    topping = input("Which topping would you like to add to your pizza? ")
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to the pizza")
        total_price+=2.5
print(f"The total price is {total_price}$")