from function_intro import Intro

def print_message():
    print("Hello world")

inclass = Intro()
inclass.escape_exit()

print_message()
print("The call result is ", Intro().multiply(5, 2))
print("The call result is ", Intro().divide(5, 2))

