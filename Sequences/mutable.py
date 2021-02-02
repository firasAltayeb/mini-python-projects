computer_parts = ["computer",
                  "monitor",
                  "mouse",
                  "keyboard"]

another_list = computer_parts
print(id(computer_parts))
print(id(another_list))

computer_parts += ["keypad"]
print(computer_parts)
print(id(computer_parts))
print(another_list)

a = b = c = another_list
a.append("cream")
print(b)
print(c)
