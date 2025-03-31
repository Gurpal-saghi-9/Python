# Original string
text = "  Hello, Python World!  "

# strip() - Removes leading and trailing whitespaces
stripped = text.strip()

# lower() - Converts to lowercase
lowered = stripped.lower()

# upper() - Converts to uppercase
uppered = stripped.upper()

# capitalize() - Capitalizes the first character
capitalized = stripped.capitalize()

# title() - Converts to title case
titled = stripped.title()

# swapcase() - Swaps case of all characters
swapped = stripped.swapcase()

# replace() - Replaces a substring with another
replaced = stripped.replace("Python", "Programming")

# split() - Splits the string into a list
split = stripped.split()

# join() - Joins elements of a list into a string
joined = "-".join(split)

# find() - Finds the first occurrence of a substring
found_index = stripped.find("Python")

# rfind() - Finds the last occurrence of a substring
rfound_index = stripped.rfind("o")

# index() - Finds the first occurrence of a substring (raises ValueError if not found)
try:
    index = stripped.index("Python")
except ValueError:
    index = -1

# rindex() - Finds the last occurrence of a substring (raises ValueError if not found)
try:
    rindex = stripped.rindex("o")
except ValueError:
    rindex = -1

# count() - Counts occurrences of a substring
count = stripped.count("o")

# startswith() - Checks if the string starts with a substring
starts_with = stripped.startswith("Hello")

# endswith() - Checks if the string ends with a substring
ends_with = stripped.endswith("World!")

# isalpha() - Checks if all characters are alphabetic
is_alpha = stripped.isalpha()

# isdigit() - Checks if all characters are digits
is_digit = stripped.isdigit()

# isalnum() - Checks if all characters are alphanumeric
is_alnum = stripped.isalnum()

# isspace() - Checks if all characters are whitespace
is_space = stripped.isspace()

# istitle() - Checks if the string is in title case
is_title = stripped.istitle()

# islower() - Checks if all characters are lowercase
is_lower = stripped.islower()

# isupper() - Checks if all characters are uppercase
is_upper = stripped.isupper()

# zfill() - Pads the string with zeros
zero_filled = stripped.zfill(30)

# ljust() - Left-justifies the string
left_justified = stripped.ljust(30, '-')

# rjust() - Right-justifies the string
right_justified = stripped.rjust(30, '-')

# center() - Centers the string
centered = stripped.center(30, '-')

# encode() - Encodes the string
encoded = stripped.encode()

# Demonstrating all results
print(f"Original: {text}")
print(f"Stripped: '{stripped}'")
print(f"Lowered: '{lowered}'")
print(f"Uppered: '{uppered}'")
print(f"Capitalized: '{capitalized}'")
print(f"Titled: '{titled}'")
print(f"Swapped: '{swapped}'")
print(f"Replaced: '{replaced}'")
print(f"Split: {split}")
print(f"Joined: '{joined}'")
print(f"Found Index: {found_index}")
print(f"Reverse Found Index: {rfound_index}")
print(f"Index: {index}")
print(f"Reverse Index: {rindex}")
print(f"Count: {count}")
print(f"Starts With 'Hello': {starts_with}")
print(f"Ends With 'World!': {ends_with}")
print(f"Is Alpha: {is_alpha}")
print(f"Is Digit: {is_digit}")
print(f"Is Alnum: {is_alnum}")
print(f"Is Space: {is_space}")
print(f"Is Title: {is_title}")
print(f"Is Lower: {is_lower}")
print(f"Is Upper: {is_upper}")
print(f"Zero Filled: '{zero_filled}'")
print(f"Left Justified: '{left_justified}'")
print(f"Right Justified: '{right_justified}'")
print(f"Centered: '{centered}'")
print(f"Encoded: {encoded}")