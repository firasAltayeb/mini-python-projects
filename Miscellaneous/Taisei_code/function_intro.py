class Intro:

    """
    number = 4
    available_exits = ["north", "south"]

    def printMessage(message, x):
        print(message * x)
        print(message * number)
    """

    # / is for division 
    def multiply(self, x, y):
        result = x * y
        return result

    # / is for division 
    def divide(self, x, y):
        result = x / y
        return result
            
    """
    def escape_exit():
        exit = ""
        while exit not in available_exits:
            exit = input("please choose an exit: ").casefold()    
            if exit.casefold() == "quit":
                print("Game Over")
                break

    escape_exit()
    

    multiply(12, 4)
    printMessage("hello world ", 2)
    """