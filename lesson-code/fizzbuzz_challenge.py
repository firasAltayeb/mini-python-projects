def fizzbuzz(number):        
    if number % 15 == 0:
        return f"fizzbuzz {number}" 
    elif number % 5 == 0:
        return f"fizz {number}"
    elif number % 3 == 0:
        return f"buzz {number}"
    else:
        return str(number)

input(f"press enter to start: ") 
print()

next_number = 0
while next_number < 30:
    next_number = next_number + 1
    print(f"ai turn: {fizzbuzz(next_number)}")


    next_number = next_number + 1
    answer = fizzbuzz(next_number)

    guess = input("your turn: ")

    if answer != guess:
        print(f"you lost, the correct answer is {answer}")
        break

print(f"well done!!! :)")