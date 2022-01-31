# f-strings
#
#
greeting = "Hello"
name = "Tim"
print(greeting + name)
age = 24
print(age)
print(type(greeting))
print(type(name))
age_in_words = "2 years"
print(name + f" is {age} years old") # add letter f before string
print(type(age))
print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.52f}")