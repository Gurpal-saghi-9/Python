# Loop with Else Approach 

num = 23

if num < 2:
    print(f"{num} is not a prime number!")

else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number!")
            break
    else:
            print(f"{num} is a prime number!")

# Function-Based Approach

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # Not prime
    return True  # Prime

num = 18
print(f"{num} is a prime number!" if is_prime(num) else f"{num} is not a prime number!")
