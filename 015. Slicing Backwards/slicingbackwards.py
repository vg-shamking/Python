# Slicing Backwards
#
#          0         1         2
#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1] # zyxwvutsrqponmlkjihgfedcb NO LETTER A as UP-TO but not included rule
print(backwards)
backwards = letters[25:-1:-1] # cannot be negative finish - no output
print(backwards)
backwards = letters[25::-1] # zyxwvutsrqponmlkjihgfedcba - LETTER A present 'cause :: - to the end
print(backwards)
backwards = letters[::-1] # zyxwvutsrqponmlkjihgfedcba - ::-1  - means all in both sides
print(backwards)
backwards = letters[25::-2] # zxvtrpnljhfdb - each second
print(backwards)
backwards = letters[16:13:-1] # qpo
print(backwards)
backwards = letters[4::-1] # edcba
print(backwards)
backwards = letters[8::-1] # ihgfedcba
print(backwards)
backwards = letters[25:17:-1] # zyxwvuts
print(backwards)
backwards = letters[:-9:-1] # zyxwvuts
print(backwards)
print()
print(letters[-4:]) # wxyz
print(letters[-1:]) # z
print(letters[1:]) # bcdefghijklmnopqrstuvwxyz
print(letters[:1]) # a - first item inn sequence
print(letters[0]) # a

