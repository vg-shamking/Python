#!/bin/python3

#Math
print(50 + 50) #add
print(50 - 50) #substract

def who_am_i():
	name = "Heath"
	age = 30
	print("My real name is " + name + " and I am " + str(age) + " years age.")
	
who_am_i()

#adding parameters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

#multiple parameters
def add(x,y):
	print(x+y)

add(7,7)

def multiply(x,y):
	return x*y

print(multiply(7,7))

def square_root(x):
	print(x ** .5)

square_root(64)

def nl():
	print('\n')

nl()

#Boolean expression (True or False)

print("Boolean expressions:")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 !=9

print (bool1, bool2, bool3, bool4)
print(type(bool1))

#Relational and Boolean Operators
nl()
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <=7
test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or = (7 > 5) or (5 > 7) #True

test_not = not True #False

#Conditional Statements
def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "NO drink for you!"

print(drink(3))
print(drink(1))

nl()

def alcohol(age,money):
	if (age>=21) and (money >=5):
		return "We've getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with money."
	elif (age < 21) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "You're too poor and too young."
print(alcohol(21,5))		
print(alcohol(21,4))
print(alcohol(20,4))
nl()
# Lists - Have brackets []
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) # starts with 0 zero
print(movies[0])
print(movies[0:4])
print(movies[1:]) # all in the list from second
print(movies[:1]) #stop at 1

nl()
#Looping
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print (x)

#while loop
i = 1
while i < 10:
	print (i)
	i += 1



