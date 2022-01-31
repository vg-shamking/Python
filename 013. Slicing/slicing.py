# Slicing in Python
#
# [0:5] UP-TO but not including
#
#         01234567890123
parrot = "Norwegian Blue"

print(parrot[0:6]) # Norweg
print(parrot[3:5]) # we
print(parrot[0:9]) # Norwegian
print(parrot[:9]) # Norwegian
# Can be [10:14] and [10:]
print(parrot[10:]) # Blue
print()
print(parrot[:6]) # Norweg
print(parrot[6:]) # ian Blue
print(parrot[:6] + parrot[6:]) # Norwegian Blue
print()
print(parrot[-6:]) # n Blue
print(parrot[:-6]) # Norwegia
print(parrot[:-6] + parrot[-6:]) # Norwegian Blue
print()
print(parrot[:]) # Norwegian Blue
print(parrot[-4:-2]) # Bl
print(parrot[-4:12]) # Bl
print(parrot[-14:-7]) # Norwegi
letters = "abcdefghijklmnopr"