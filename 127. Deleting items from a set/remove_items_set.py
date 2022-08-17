small_ints = set(range(21))
print(small_ints)

# small_ints.clear()  #set()
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99)
print(small_ints)

# small_ints.remove(99)  # KeyError: 99 - there is no 99 in the set
# print(small_ints)

