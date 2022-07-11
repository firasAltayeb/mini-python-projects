class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle("Kenwood", 9.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.5
print(kenwood.price)

hamilton = Kettle("Hamilton", 15.0)

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamliton))
