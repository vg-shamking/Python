data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_value = 100
max_value = 200

# for index in range(len(data) - 1, - 1, -1):
#         if data[index] < min_value or data[index] > max_value:
#             print(index, data)
#             del data[index]

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_value or value > max_value:
        print(top_index - index, value)
        del data[top_index - index]

print(data)
