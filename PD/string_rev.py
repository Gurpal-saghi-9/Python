str = "Gurpal"

reversed_str = str[::-1]

print(reversed_str)  

str = "Gurpal"

rev = "".join(reversed(str))

print(rev)


string = "Hello, World!"
reversed_str = ""
for char in string:
    reversed_str =   char + reversed_str 

print(reversed_str)