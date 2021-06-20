with open("new_aozora_text.txt", encoding='utf-8', errors='ignore') as file:
    lines = [line.rstrip('\n') for line in file]

body_text = ''.join(lines).replace("―", "").replace("　", "")
sentences = body_text.split('。')

# print(*sentences, sep="\n")
five_char_sen_counter = 0
six_char_sen_counter = 0
seven_char_sen_counter = 0
eight_char_sen_counter = 0
nine_char_sen_counter = 0
ten_char_sen_counter = 0
eleven_char_sen_counter = 0
twelve_char_sen_counter = 0
thirteen_char_sen_counter = 0
fourteen_char_sen_counter = 0
fifteen_char_sen_counter = 0
sixteen_char_sen_counter = 0
seventeen_char_sen_counter = 0
eighteen_char_sen_counter = 0
nineteen_char_sen_counter = 0
twenty_char_sen_counter = 0
twenty_one_char_sen_counter = 0
twenty_two_char_sen_counter = 0
twenty_three_char_sen_counter = 0
twenty_four_char_sen_counter = 0
twenty_five_char_sen_counter = 0

for sentence in sentences:
    print(sentence)
    if len(sentence) == 5:
        five_char_sen_counter += 1
    elif len(sentence) == 6:
        six_char_sen_counter += 1
    elif len(sentence) == 7:
        seven_char_sen_counter += 1
    elif len(sentence) == 8:
        eight_char_sen_counter += 1
    elif len(sentence) == 9:
        nine_char_sen_counter += 1
    elif len(sentence) == 10:
        ten_char_sen_counter += 1
    elif len(sentence) == 11:
        eleven_char_sen_counter += 1
    elif len(sentence) == 12:
        twelve_char_sen_counter += 1
    elif len(sentence) == 13:
        thirteen_char_sen_counter += 1
    elif len(sentence) == 14:
        fourteen_char_sen_counter += 1
    elif len(sentence) == 15:
        fifteen_char_sen_counter += 1
    elif len(sentence) == 16:
        sixteen_char_sen_counter += 1
    elif len(sentence) == 17:
        seventeen_char_sen_counter += 1
    elif len(sentence) == 18:
        eighteen_char_sen_counter += 1
    elif len(sentence) == 19:
        nineteen_char_sen_counter += 1
    elif len(sentence) == 20:
        twenty_char_sen_counter += 1
    elif len(sentence) == 21:
        twenty_one_char_sen_counter += 1
    elif len(sentence) == 22:
        twenty_two_char_sen_counter += 1
    elif len(sentence) == 23:
        twenty_three_char_sen_counter += 1
    elif len(sentence) == 24:
        twenty_four_char_sen_counter += 1
    elif len(sentence) == 25:
        twenty_five_char_sen_counter += 1

    with open('new_analysed_text.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "。\n")

        if sentences[-1] == sentence:
            new_file.write("Number of five character long sentence is {} \n".format(five_char_sen_counter))
            new_file.write("Number of six character long sentence is {} \n".format(five_char_sen_counter))
            new_file.write("Number of seven character long sentence is {} \n".format(five_char_sen_counter))
            new_file.write("Number of eight character long sentence is {} \n".format(five_char_sen_counter))
            new_file.write("Number of nine character long sentence is {} \n".format(five_char_sen_counter))
            new_file.write("Number of ten character long sentence is {} \n".format(five_char_sen_counter))
            new_file.write("Number of eleven character long sentence is {} \n".format(eleven_char_sen_counter))
            new_file.write("Number of twelve character long sentence is {} \n".format(twelve_char_sen_counter))
            new_file.write("Number of thirteen character long sentence is {} \n".format(thirteen_char_sen_counter))
            new_file.write("Number of fourteen character long sentence is {} \n".format(fourteen_char_sen_counter))
            new_file.write("Number of fifteen character long sentence is {} \n".format(fifteen_char_sen_counter))
            new_file.write("Number of sixteen character long sentence is {} \n".format(sixteen_char_sen_counter))
            new_file.write("Number of seventeen character long sentence is {} \n".format(seventeen_char_sen_counter))
            new_file.write("Number of eighteen character long sentence is {} \n".format(eighteen_char_sen_counter))
            new_file.write("Number of nineteen character long sentence is {} \n".format(nineteen_char_sen_counter))
            new_file.write("Number of twenty character long sentence is {} \n".format(twenty_char_sen_counter))
            new_file.write("Number of twenty one character long sentence is {} \n".format(twenty_one_char_sen_counter))
            new_file.write("Number of twenty two character long sentence is {} \n".format(twenty_two_char_sen_counter))
            new_file.write(
                "Number of twenty three character long sentence is {} \n".format(twenty_three_char_sen_counter))
            new_file.write(
                "Number of twenty four character long sentence is {} \n".format(twenty_four_char_sen_counter))
            new_file.write(
                "Number of twenty five character long sentence is {} \n".format(twenty_five_char_sen_counter))
