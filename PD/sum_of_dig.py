# iterative approach
dig = 12345

sum_of_dig = 0

print(f"Sum of Digits {dig} : ", end="")

while dig:
    sum_of_dig += dig % 10 # extract krda last digit nu ate sum ch add krda
    dig //= 10 # remove krda last digit nu

print(f"{sum_of_dig}")

# Recursive Approach

def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

dig = 762
print(f"Sum of Digits {dig} : {sum_of_dig}")
