shopping_list = ["milk", "pasta", "spam", "eggs"]

item_to_fine = "spam"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_fine:
#         found_at = index
#         break

if item_to_fine in shopping_list:
    found_at = shopping_list.index(item_to_fine)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_fine))
