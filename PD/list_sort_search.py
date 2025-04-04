list = [12, 56, 76, 45, 87, 47, 36]

print(f"Before sortinga list : {list}")

for j in range(len(list) - 1):
        for k in range(len(list) - j - 1):
            if list[k] > list[k + 1]:
                list[k], list[k + 1] = list[k + 1], list[k]

print("Sorted list using loop:", list)

list.sort()
print("Sorted list using sort function:", list)

num = 45
if num in list:
    print(f"{num} found at index {list.index(num)}")
else:
    print(f"{num} not found in the list")