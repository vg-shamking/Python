farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print()
print("Indexing a sequence")
animal_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animal_list[3]
print(goat)

# print("Indexing a set is not possible")
# goat = farm_animals[3]  # TypeError: 'set' object is not subscriptable

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}
if more_animals == farm_animals:
    print('The sets are equal')
else:
    print('Sets are different')  # Order is not important <- sets are same

