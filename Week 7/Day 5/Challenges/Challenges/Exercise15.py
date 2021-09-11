def common_div(num1,num2):
    common_divisors = []
    for i in range(2,num1+1):
        if num1%i == 0 and num2%i ==0:
            common_divisors.append(i)
    return common_divisors
print(common_div(10,20))
print(common_div(1500,5000))