class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 9.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.5
print(kenwood.price)

hamilton = Kettle("Hamilton", 15.0)

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()

Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)
# classes in python are dynamic
kenwood.power = 1.5
print(kenwood.power)

