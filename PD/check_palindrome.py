str = "madam"

dupstr = str[::-1]

print("Palindrome" if str == dupstr else "Not Palindrome")

if str == dupstr:
    print("Is palindrome")
else:
    print("Not palindrome")