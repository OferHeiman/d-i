def factorial(num):
    factorial_sum = 1
    for i in range(1,num+1):
        factorial_sum = factorial_sum*i
    return factorial_sum
print(factorial(4))