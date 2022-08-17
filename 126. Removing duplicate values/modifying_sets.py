numbers = set()

print(numbers, type(numbers))

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from the list, to remove duplicates.
unique_data = sorted(set(data))
print(unique_data)

# Create a list of unique colours, keeping the order they appeared.
unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))
