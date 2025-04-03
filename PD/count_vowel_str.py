str = "This is a string, For counting the vowels."

vowels = "aeiouAEIOU"
count = sum(1 for char in str if char in vowels)
print(count)

count = 0
for char in str:
    if char in vowels:
        count += 1
print(count)