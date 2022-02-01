# if
#   elif
#       else
answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess lower")
else:   # goes only after if and elif read / if and elif will be always read
    print("You got it first time")

