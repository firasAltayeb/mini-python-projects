import time
import concurrent.futures

from allowed_characters import kana_List

MAX_THREADS = 10

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


def length_counter(sentence):
    print('counting..' + sentence)
    number_of_chara = 0
    furigana_bracket_found = False

    for character in sentence:
        if character == '（':
            furigana_bracket_found = True
        if not furigana_bracket_found and character in kana_List:
            number_of_chara += 1
        if character == '）':
            furigana_bracket_found = False

    if number_of_chara == 6:
        global six_char_sen_counter
        six_char_sen_counter += 1
    elif number_of_chara == 7:
        global seven_char_sen_counter
        seven_char_sen_counter += 1
    elif number_of_chara == 8:
        global eight_char_sen_counter
        eight_char_sen_counter += 1
    elif number_of_chara == 9:
        global nine_char_sen_counter
        nine_char_sen_counter += 1
    elif number_of_chara == 10:
        global ten_char_sen_counter
        ten_char_sen_counter += 1
    elif number_of_chara == 11:
        global eleven_char_sen_counter
        eleven_char_sen_counter += 1
    elif number_of_chara == 12:
        global twelve_char_sen_counter
        twelve_char_sen_counter += 1
    elif number_of_chara == 13:
        global thirteen_char_sen_counter
        thirteen_char_sen_counter += 1
    elif number_of_chara == 14:
        global fourteen_char_sen_counter
        fourteen_char_sen_counter += 1
    elif number_of_chara == 15:
        global fifteen_char_sen_counter
        fifteen_char_sen_counter += 1
    elif number_of_chara == 16:
        global sixteen_char_sen_counter
        sixteen_char_sen_counter += 1
    elif number_of_chara == 17:
        global seventeen_char_sen_counter
        seventeen_char_sen_counter += 1
    elif number_of_chara == 18:
        global eighteen_char_sen_counter
        eighteen_char_sen_counter += 1
    elif number_of_chara == 19:
        global nineteen_char_sen_counter
        nineteen_char_sen_counter += 1
    elif number_of_chara == 20:
        global twenty_char_sen_counter
        twenty_char_sen_counter += 1
    elif number_of_chara == 21:
        global twenty_one_char_sen_counter
        twenty_one_char_sen_counter += 1
    elif number_of_chara == 22:
        global twenty_two_char_sen_counter
        twenty_two_char_sen_counter += 1
    elif number_of_chara == 23:
        global twenty_three_char_sen_counter
        twenty_three_char_sen_counter += 1
    elif number_of_chara == 24:
        global twenty_four_char_sen_counter
        twenty_four_char_sen_counter += 1
    elif number_of_chara == 25:
        global twenty_five_char_sen_counter
        twenty_five_char_sen_counter += 1
    elif number_of_chara == 26:
        global twenty_six_char_sen_counter
        twenty_six_char_sen_counter += 1
    elif number_of_chara == 27:
        global twenty_seven_char_sen_counter
        twenty_seven_char_sen_counter += 1
    elif number_of_chara == 28:
        global twenty_eight_char_sen_counter
        twenty_eight_char_sen_counter += 1
    elif number_of_chara == 29:
        global twenty_nine_char_sen_counter
        twenty_nine_char_sen_counter += 1
    elif number_of_chara == 30:
        global thirty_char_sen_counter
        thirty_char_sen_counter += 1


def concurrent_run(sens):
    threads = min(MAX_THREADS, len(sens))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(length_counter, sens)

    with open('n5_muke_sentences.txt', 'a+', encoding='utf-8') as new_file:
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


def main(sens):
    t0 = time.time()
    concurrent_run(sens)
    t1 = time.time()
    print(f"{t1 - t0} seconds to analyse {len(sens)} stories.")


with open("n5_muke_sentences.txt", encoding='utf-8', errors='ignore') as file:
    lines = [line.rstrip('\n') for line in file]

main(lines)
