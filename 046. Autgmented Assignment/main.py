# IntelliJ and PyCharm highlight errors

# Augmented assignment sounds really fancy, but it's just a shorthand way of assigning
# values to a variable.

# line 35: guesses = guesses + 1 should be (and was) changed to guesses += 1
#
# # Hi Lo game
#
# low = 1
# high = 1000
#
# print("Please think of number between {} and {}".format(low, high))
# input("Press ENTER to start")
#
# guesses = 1
# while True:
#     print("\tGuessing in the range of {} to {}".format(low, high))
#     guess = low + (high - low) // 2
#     high_low = input("My guess is {}. Should I guess higher or lower? "
#                     "Enter h or l, or c if my guess was correct "
#                      .format(guess)).casefold()
#
#     if high_low == "h":
#         # Guess higher. The low end of the range becomes 1 greater than the guess.
#         low = guess + 1
#     elif high_low == "l":
#         # Guess lower. The low end of the range becomes 1 greater than the guess.
#         high = guess - 1
#     elif high_low == "c":
#         print("I got it in {} guesses!".format(guesses))
#         break
#     else:
#         print("Please enter h, l or c")
#     guesses += 1
x = 23

x += 1
print(x)    # 24

x -= 4
print(x)    # 20

x *= 5
print(x)    # 100

x //= 4
print(x)    # 25

x /= 5
print(x)    # 5.0

x **= 2
print(x)    # 25.0

x %= 5
print(x)    # 0.0

greeting = "Good "

greeting += "morning"
print(greeting)

greeting *= 5
print(greeting)
