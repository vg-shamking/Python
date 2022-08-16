numbers = set()

print(numbers, type(numbers))

# numbers.add(1)
# print(numbers)

while len(numbers) < 4:
    next_value = int(input("Please enter your next values: "))
    numbers.add(next_value)
print(numbers)  # only new numbers - no duplicates

