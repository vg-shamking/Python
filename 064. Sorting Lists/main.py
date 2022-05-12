even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print(id(even))  # id = 2543925341888 (changes each time)
print(id(odd))  # id = 2543925341696 (changes each time)
even.extend(odd)
print(even)
another_even = even
print(another_even)
print(id(another_even))

even.sort(reverse=True)
print(even)
print(another_even)
print(id(even))  # same id
print(id(odd))  # same id
print(id(another_even))  # same as even


