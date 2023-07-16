def conditional_diff_first(condition):
    if condition == True:
        print("first condition is satisfied")
    elif condition == False:
        print("first condition is not satisfactory")


def conditional_diff_second(condition):
    if condition == True:
        print("second condition is satisfied")
    if condition == False:
        print("second condition is not satisfied")
    else:
        print("second condition is not satisfactory")


conditional_diff_first(True)
conditional_diff_second(True)
