# Iterative Approach

num = 5
result = 1
for i in range(2, num + 1):
    result *= i
print(f"Factorial of a {num} is : {result}")  # Output: 120

# 

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

num = 7
print(f"Factorial of a {num} is : {factorial_recursive(num)}")  # Output: 5040

# Built in function
import math
num = 3
print(f"Factorial of a {num} is : {math.factorial(num)}") # Output: 6