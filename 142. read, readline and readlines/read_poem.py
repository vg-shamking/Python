# This code prints out reversed lines of poem
#
# with open('Jabberwocky.txt', 'r') as jabber:
#     lines = jabber.readlines()  # list of strings
#
# # print(lines)
#
# for line in reversed(lines):
#     print(line, end='')  # prints poem reversely

# ----------------------------------------------------------
# It prints out completely reversed text:
#
# with open('Jabberwocky.txt', 'r') as jabber:
#     text = jabber.read()
#
# # print(text)
# for character in reversed(text):
#     print(character, end='')
#
# ----------------------------------------------------------
# Code for looking special word in text
# (goes up-to the place with needed word) "jubjub in this case
#
with open('Jabberwocky.txt') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)

with open('Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break
