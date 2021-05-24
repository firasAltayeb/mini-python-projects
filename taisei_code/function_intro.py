class Intro:
    number = 4
    available_exits = ["north", "south"]

    def printMessage(self, message, x):
        print(message * x)
        print(message * self.number)
    

    # / is for division
    def multiply(self, x, y):
        result = x * y
        return result

    # / is for division 
    def divide(self, x, y):
        result = x / y
        return result
            
    
    def escape_exit(self):
        exit = ""
        while exit not in self.available_exits:
            exit = input("please choose an exit: ").casefold()    
            if exit.casefold() == "quit":
                print("Game Over")
                break
        print("You have escaped")
    

