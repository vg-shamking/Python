from enemy3 import Enemy, Troll

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll), end="\n")

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

# monster = Enemy("Basic enemy")
# monster.grunt()
# Traceback (most recent call last):
#   File "C:\Users\MGorb\Desktop\Python\STUDY_Python\224. Calling Super Methods\main.py", line 17, in <module>
#     monster.grunt()
# AttributeError: 'Enemy' object has no attribute 'grunt'