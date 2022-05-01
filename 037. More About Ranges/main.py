# #
# # for i in range(10, 0, -2):
# #     print("i is now {}".format(i))
age = int(input("How old are you? "))

if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age >65:
    print("Enjoy your free time")
else:
    print("Have a good dat at work")
