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

for meal in menu:
    if "dog" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print("{0} has a dog score of {1}".format(meal, meal.count("dog")))