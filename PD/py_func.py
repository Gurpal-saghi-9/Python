# Print name
def greet(name = "Python"):
    print(f"Hello {name}")

# name = input("Enter your name: ")
# greet(name)

# greet("World")  

# greet()

# swap two numbers

def swap(a, b):
    return b, a
a =12
b = 34
print("Before swap:", a, b)
a, b = swap(a, b)
print("After swap:", a, b)
