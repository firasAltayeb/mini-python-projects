menu = [
    ["cheese", "dog"],
    ["cheese", "dog", "bread"],
    ["cheese", "bread"],
    ["cheese", "dog", "pickles"],
    ["cheese", "pickles"],
    ["pickles", "dog"],
    ["pickles", "bread",],
    ["cheese", "dog", "dog", "dog", "bread", "pickles"],
]

# for meal in menu:
#     for item in meal:
#         if item != "dog":
#             print(item, end=" ")          
#     print()


for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "dog":
            del meal[index] 
            
    print(", ".join(meal))