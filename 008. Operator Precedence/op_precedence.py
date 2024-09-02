#  PEMDAS -> Parentheses Exponents Multiplication/Division Addition/Subtraction
#  BEDMAS -> Brackets Exponents Division/Multiplication Addition/Subtraction
#  BODMAS -> Brackets Order Division/Multiplication Addition/Subtraction
#  BIDMAS -> Brackets Index Division/Multiplication Addition/Subtraction

a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

print()

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3 - 4) * 12))
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) /b)
