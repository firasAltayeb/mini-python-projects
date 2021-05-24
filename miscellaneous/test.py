def john_mary(str):
    john_counter = 0
    mary_counter = 0
    john = 'john'
    mary = 'mary'
    sub_john = len(john)
    sub_mary = len(mary)

    lower_str = str.casefold()
    print(lower_str)

    for i in range(len(lower_str)):
        if lower_str[i:i+sub_john] == "mary":
            mary_counter += 1
            print("mary counter is {}".format(mary_counter))
        if lower_str[i:i+sub_mary].casefold() == "john":
            john_counter += 1
            print("john counter is {}".format(john_counter))
    return mary_counter == john_counter


print(john_mary('John&Mary'))
