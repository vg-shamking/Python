# # for i in range(10):
# #     print("i is now {}".format(i))
#
# i = 0
# while True:
#     print("i is now {}".format(i))
# i += 1

available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

print("aren't you glad to got aou of there")
