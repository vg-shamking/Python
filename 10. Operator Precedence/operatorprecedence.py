# Operator Precedence explanation
#
#
# PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Substraction
# BEDMAS - Brackets, Exponents, Divisions/Multiplication, Addition/Substraction
# BODMAS - Brackets, Order, Divisions/Multiplication, Addition/Substraction
# BIDMAS - Brackets, Index, Divisions/Multiplication, Addition/Substraction

a = 12
b = 3
print(a + b / 3 - 4 * 12)
print (a + (b/3) - (4*12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()
print(a / (b * a) / b)