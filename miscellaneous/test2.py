class Greeter:

    def __init__(self, boss):
        self.boss = boss
        self.last_greeted_visitor = ''
        self.visitors_list = []
        pass

    def enters(self, visitor=''):
        if visitor != '':
            self.visitors_list.append(visitor)
        return None

    def greet(self):
        last_visitor = self.visitors_list[-1]
        if self.last_greeted_visitor != last_visitor:
            self.last_greeted_visitor = last_visitor
            if last_visitor == self.boss:
                return "Hello, {}".format(self.boss)
            elif last_visitor != '':
                return "Welcome, {}".format(last_visitor)
        return


g = Greeter('Chuck')
g.enters('John')
g.enters('Chuck')
g.enters('Mary')
print(g.greet())
g.enters('Mary')
print(g.greet())
