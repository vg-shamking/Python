# Introduction to Blocks and Statements
#
#
# Levels of blocks: for - first leve, try - second level; block within second block is third block
# all that follows : is identified as second block
#
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80) # with TAB and WITHOUT on this line gives very different results
print()
print("*" * 80)
