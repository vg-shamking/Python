# if Challenge
#
#
name = input("What is your name? ")
age = int(input("What is your age? "))
# if 18 <= age < 31
if age >= 18 and age <= 30:
    print("{0}, you're welcomed to the holiday.".format(name))
else:
    print("{0}, you are refused to enter".format(name))