with open("full_aozora_text.txt", encoding='utf-8', errors='ignore') as file:
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
twenty_six_char_sen_counter = 0
twenty_seven_char_sen_counter = 0
twenty_eight_char_sen_counter = 0
twenty_nine_char_sen_counter = 0
thirty_char_sen_counter = 0

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
    elif len(sentence) == 26:
        twenty_five_char_sen_counter += 1
    elif len(sentence) == 27:
        twenty_five_char_sen_counter += 1
    elif len(sentence) == 28:
        twenty_five_char_sen_counter += 1
    elif len(sentence) == 29:
        twenty_five_char_sen_counter += 1
    elif len(sentence) == 30:
        twenty_five_char_sen_counter += 1

    with open('new_analysed_text.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "。\n")

        if sentences[-1] == sentence:
            new_file.write("# of five char long sentence is {} \n".format(five_char_sen_counter))
            new_file.write("# of six char long sentence is {} \n".format(six_char_sen_counter))
            new_file.write("# of seven char long sentence is {} \n".format(seven_char_sen_counter))
            new_file.write("# of eight char long sentence is {} \n".format(eight_char_sen_counter))
            new_file.write("# of nine char long sentence is {} \n".format(nine_char_sen_counter))
            new_file.write("# of ten char long sentence is {} \n".format(ten_char_sen_counter))
            new_file.write("# of eleven char long sentence is {} \n".format(eleven_char_sen_counter))
            new_file.write("# of twelve char long sentence is {} \n".format(twelve_char_sen_counter))
            new_file.write("# of thirteen char long sentence is {} \n".format(thirteen_char_sen_counter))
            new_file.write("# of fourteen char long sentence is {} \n".format(fourteen_char_sen_counter))
            new_file.write("# of fifteen char long sentence is {} \n".format(fifteen_char_sen_counter))
            new_file.write("# of sixteen char long sentence is {} \n".format(sixteen_char_sen_counter))
            new_file.write("# of seventeen char long sentence is {} \n".format(seventeen_char_sen_counter))
            new_file.write("# of eighteen char long sentence is {} \n".format(eighteen_char_sen_counter))
            new_file.write("# of nineteen char long sentence is {} \n".format(nineteen_char_sen_counter))
            new_file.write("# of twenty char long sentence is {} \n".format(twenty_char_sen_counter))
            new_file.write("# of twenty one char long sentence is {} \n".format(twenty_one_char_sen_counter))
            new_file.write("# of twenty two char long sentence is {} \n".format(twenty_two_char_sen_counter))
            new_file.write("# of twenty three char long sentence is {} \n".format(twenty_three_char_sen_counter))
            new_file.write("# of twenty four char long sentence is {} \n".format(twenty_four_char_sen_counter))
            new_file.write("# of twenty five char long sentence is {} \n".format(twenty_five_char_sen_counter))
            new_file.write("# of twenty six char long sentence is {} \n".format(twenty_six_char_sen_counter))
            new_file.write("# of twenty seven char long sentence is {} \n".format(twenty_seven_char_sen_counter))
            new_file.write("# of twenty eight char long sentence is {} \n".format(twenty_eight_char_sen_counter))
            new_file.write("# of twenty nine char long sentence is {} \n".format(twenty_nine_char_sen_counter))
            new_file.write("# of thirty char long sentence is {} \n".format(thirty_char_sen_counter))
