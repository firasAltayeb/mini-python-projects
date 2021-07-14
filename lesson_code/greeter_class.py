class GreeterJames:
    to_greet_list = []
    time_of_day = "Morning"

    def change_time(self, time):
        self.time_of_day = time

    def enters(self, visitor):
        self.to_greet_list.append(visitor)

    def greet(self):
        # visitors_list = [1, 2, 3, 4, 5]
        for visitor in self.to_greet_list:
            if self.time_of_day == "Morning":
                print("Good morning {}".format(visitor))
            elif self.time_of_day == "Afternoon":
                print("Good afternoon {}".format(visitor))
            elif self.time_of_day == "Evening":
                print("Good evening {}".format(visitor))
        self.to_greet_list.clear()


class GreeterMark:
    visitors_list = []

    def enters(self, visitor):
        self.visitors_list.append(visitor)

    def greet(self):
        print("Hello {}-san"
              .format(self.visitors_list[0]))


class GreeterHaruna:
    v_list = []

    def enters(self, visitor):
        self.v_list.append(visitor)

    def greet(self):
        print("Hi " + (self.v_list[0]))
