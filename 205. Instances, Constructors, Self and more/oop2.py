# a = 12
# b = 4
# print(a + b)
# print(a.__add__(b))

class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print("Original :", kenwood.price)

kenwood.price = 12.75
print("New :", kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print(hamilton.make)
print(hamilton.price)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

kenwood.power = 1.5
print_(kenwood.power)
print(hamilton.power)
