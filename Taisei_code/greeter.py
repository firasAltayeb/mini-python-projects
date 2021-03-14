class Greeter:
    visitors_list = []
    
    def enters(self, visitor):
        self.visitors_list.append(visitor)

    def greet(self):
        print("Good afternoon {}"
            .format(self.visitors_list[0]))