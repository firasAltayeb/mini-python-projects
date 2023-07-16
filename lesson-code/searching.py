bird_types = ["Blue Jay", "American Robin", "Sparrow", "Owl", "Pigeon"]
item_to_find = "Sparrow"
found_at = None

# for index in range(len(bird_types)):
#     if bird_types[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in bird_types:
    found_at = bird_types.index(item_to_find)

if found_at is not None:
    print("item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))