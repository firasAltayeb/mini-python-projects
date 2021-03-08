"""
print("Hello World")
name = input("Please Enter Your Name \n")

print(name)

i = 0
while i < 10: 
    print("I is now " + str(i))
    i = i + 1
"""

available_exits = ["north", "south"]

exit = ""
while exit not in available_exits:
    exit = input("please choose an exit: ").casefold()    
    if exit.casefold() == "quit":
        print("Game Over")
        break
else: print("you have escaped with else")
"""
if exit.casefold() in available_exits:
    print("you have escaped")
"""