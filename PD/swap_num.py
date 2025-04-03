num1 = 23
num2 = 32

print(f"Before swaping : {num1, num2}")

# Approach 1 : Using Python's Tuple Unpacking

num1, num2 = num2, num1
print(f"After swaping without using third variable : {num1 , num2}")

# Approach 2 : Using Arithmetic Operations (+ and -)

num1 = 23
num2 = 32

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(f"After swaping using arithmetic operation (+,-) : {num1 , num2}")

# Approach 3 : Using Arithmetic Operations (* and //) (Only for Non-Zero b)

num1 = 23
num2 = 32

num1 = num1 * num2
num2 = num1 // num2
num1 = num1 // num2
print(f"After swaping using arithmetic operation (*,//) : {num1 , num2}")

# Approach 4 : Using a Temporary Variable

num1 = 23
num2 = 32

temp = num1
num1 = num2
num2 = temp
print(f"After swaping using third variable : {num1 , num2}")

# Approach 5 : Using Bitwise XOR (^)

num1 = 23
num2 = 32

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print(f"After swapping using Bitwise XOR: {num1}, {num2}")
