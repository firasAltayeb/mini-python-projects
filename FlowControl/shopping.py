shopping_list = ["milk", "pasta", "spam", "eggs"]

for item in shopping_list:
    if item != "spam":
        print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)

