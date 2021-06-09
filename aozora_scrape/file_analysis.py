with open("aozora_text.txt", encoding='utf-8') as file:
    body_text = file.read().replace('\n', '')

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
    elif len(sentence) == 5:
        six_char_sen_counter += 1
    elif len(sentence) == 5:
        seventeen_char_sen_counter += 1
    elif len(sentence) == 5:
        eight_char_sen_counter += 1
    elif len(sentence) == 5:
        nine_char_sen_counter += 1
    elif len(sentence) == 5:
        ten_char_sen_counter += 1
    elif len(sentence) == 5:
        eleven_char_sen_counter += 1
    elif len(sentence) == 5:
        twelve_char_sen_counter += 1
    elif len(sentence) == 5:
        thirteen_char_sen_counter += 1
    elif len(sentence) == 5:
        fourteen_char_sen_counter += 1
    elif len(sentence) == 5:
        fifteen_char_sen_counter += 1
    elif len(sentence) == 5:
        sixteen_char_sen_counter += 1
    elif len(sentence) == 5:
        seventeen_char_sen_counter += 1
    elif len(sentence) == 5:
        eighteen_char_sen_counter += 1
    elif len(sentence) == 5:
        nineteen_char_sen_counter += 1
    elif len(sentence) == 5:
        twenty_char_sen_counter += 1
    elif len(sentence) == 5:
        twenty_one_char_sen_counter += 1
    elif len(sentence) == 5:
        twenty_two_char_sen_counter += 1
    elif len(sentence) == 5:
        twenty_three_char_sen_counter += 1
    elif len(sentence) == 5:
        twenty_four_char_sen_counter += 1
    elif len(sentence) == 5:
        twenty_five_char_sen_counter += 1

    with open('new_aozora_text.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")
