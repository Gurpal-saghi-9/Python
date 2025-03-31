n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")  # Print leading spaces
    for j in range(1, 2 * i):   # Print numbers
        print(j, end="")
    print()  # Move to the next line
