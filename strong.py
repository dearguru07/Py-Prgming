def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_strong_number(num):
    sum_of_factorials = 0
    temp = num
    
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += factorial(digit)
        temp //= 10
    
    return sum_of_factorials == num

number = int(input("Enter a number: "))
if is_strong_number(number):
    print(f"{number} is a Strong Number.")
else:
    print(f"{number} is not a Strong Number.")
