# Using a Step in a Slice
#
# [0:5:3] Meaning of slice step
#
#         01234567890123
parrot = "Norwegian Blue"

print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw
print()
number = "9,223,372,036,854,775,807"
print(number[1::4]) # starting from first character show every fourth char
print(number[3::5]) # 22,70
number = "9,223;372:036 854,775;807"
print(number[1::4]) # ,;: ,;
print()
separators = number[1::4]
print(separators)
print()
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print()
