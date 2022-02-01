# Conditional Operators
#
# less than                 <
# Less than or equal to     <=
# Greater than              >
# Greater than or equal to  >=
# Equal to                  ==
# Not equal to              !=
#
answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you've not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:   # goes only after if and elif read / if and elif will be always read
#     print("You got it first time")
