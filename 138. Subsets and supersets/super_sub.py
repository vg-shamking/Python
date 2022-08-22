animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat'
           }

birds = {'Robin', 'Swallow', 'Wren'}

print(f'birds is a subset of animals: {birds.issubset(animals)}')  # True
print(f'animals is a superset of birds: {animals.issuperset(birds)}')  # True

print(f'birds is a superset of animals: {birds.issuperset(animals)}')  # False

print(birds <= animals)  # True
print(birds < animals)  # True

print('*' * 80)

garden_birds = {'Robin', 'Swallow', 'Wren'}
print(garden_birds == birds)  # True
print(garden_birds <= birds)  # True: garden_birds is a subset of birds
print(garden_birds < birds)  # False: not a superset

print('*' * 80)

more_birds = {'Wren', 'Budgie', 'Swallow'}
print(garden_birds >= more_birds)  # False: garden_birds is not a superset of more_birds
