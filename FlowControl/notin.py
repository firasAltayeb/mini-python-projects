activity = input("what would you like to do today? ")

if "cinema" not in activity.casefold():
    print("But i want to go to the cinema")
else:
    print("let's go bro")

name = input("what's your name? ")

age = int(input("how old are you dude? "))

if 18 <= age <= 35:
    print("let's party {}".format(name))
