import time
import concurrent.futures
from allowed_characters import open_list
from allowed_characters import close_list

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
    print('analysing..' + sentence)
    if len(sentence) == 6:
        global six_char_sen_counter
        six_char_sen_counter += 1
    elif len(sentence) == 7:
        global seven_char_sen_counter
        seven_char_sen_counter += 1
    elif len(sentence) == 8:
        global eight_char_sen_counter
        eight_char_sen_counter += 1
    elif len(sentence) == 9:
        global nine_char_sen_counter
        nine_char_sen_counter += 1
    elif len(sentence) == 10:
        global ten_char_sen_counter
        ten_char_sen_counter += 1
    elif len(sentence) == 11:
        global eleven_char_sen_counter
        eleven_char_sen_counter += 1
    elif len(sentence) == 12:
        global twelve_char_sen_counter
        twelve_char_sen_counter += 1
    elif len(sentence) == 13:
        global thirteen_char_sen_counter
        thirteen_char_sen_counter += 1
    elif len(sentence) == 14:
        global fourteen_char_sen_counter
        fourteen_char_sen_counter += 1
    elif len(sentence) == 15:
        global fifteen_char_sen_counter
        fifteen_char_sen_counter += 1
    elif len(sentence) == 16:
        global sixteen_char_sen_counter
        sixteen_char_sen_counter += 1
    elif len(sentence) == 17:
        global seventeen_char_sen_counter
        seventeen_char_sen_counter += 1
    elif len(sentence) == 18:
        global eighteen_char_sen_counter
        eighteen_char_sen_counter += 1
    elif len(sentence) == 19:
        global nineteen_char_sen_counter
        nineteen_char_sen_counter += 1
    elif len(sentence) == 20:
        global twenty_char_sen_counter
        twenty_char_sen_counter += 1
    elif len(sentence) == 21:
        global twenty_one_char_sen_counter
        twenty_one_char_sen_counter += 1
    elif len(sentence) == 22:
        global twenty_two_char_sen_counter
        twenty_two_char_sen_counter += 1
    elif len(sentence) == 23:
        global twenty_three_char_sen_counter
        twenty_three_char_sen_counter += 1
    elif len(sentence) == 24:
        global twenty_four_char_sen_counter
        twenty_four_char_sen_counter += 1
    elif len(sentence) == 25:
        global twenty_five_char_sen_counter
        twenty_five_char_sen_counter += 1
    elif len(sentence) == 26:
        global twenty_six_char_sen_counter
        twenty_six_char_sen_counter += 1
    elif len(sentence) == 27:
        global twenty_seven_char_sen_counter
        twenty_seven_char_sen_counter += 1
    elif len(sentence) == 28:
        global twenty_eight_char_sen_counter
        twenty_eight_char_sen_counter += 1
    elif len(sentence) == 29:
        global twenty_nine_char_sen_counter
        twenty_nine_char_sen_counter += 1
    elif len(sentence) == 30:
        global thirty_char_sen_counter
        thirty_char_sen_counter += 1

    with open('new_analysed_text.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")


def reverse_balance(sentence):
    stack = []
    newest_sentence = ""
    print(" reverse_balance sentence is {}".format(sentence))
    for i in sentence[::-1]:
        if i not in open_list and i not in close_list:
            newest_sentence = i + newest_sentence
        if i in close_list:
            stack.append(i)
            newest_sentence = i + newest_sentence
        elif i in open_list:
            pos = open_list.index(i)
            if ((len(stack) > 0) and
                    (close_list[pos] == stack[len(stack) - 1])):
                stack.pop()
                newest_sentence = i + newest_sentence
            else:
                print("Excluding ", i)

    if len(newest_sentence) < 6:
        return

    print("stack length is {}".format(len(stack)))
    if len(stack) == 0 and newest_sentence not in new_seen_set:
        new_seen_set.add(newest_sentence)
        length_counter(newest_sentence)


def check_balance(sentence):
    stack = []
    new_sentence = ""
    print("check_balance sentence is {}".format(sentence))
    for i in sentence:
        if i not in open_list and i not in close_list:
            new_sentence += i
        if i in open_list:
            stack.append(i)
            new_sentence += i
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
                new_sentence += i
            else:
                print("Excluding ", i)

    if len(new_sentence) < 6:
        return

    print("stack length is {}".format(len(stack)))
    if len(stack) == 0 and new_sentence not in new_seen_set:
        new_seen_set.add(new_sentence)
        length_counter(new_sentence)
    else:
        reverse_balance(new_sentence)


def concurrent_run(sens):
    bracket_list = ["（）席類製造）（", "（）席類製造", "（）席類{}製造", "席類製造（", "]席[類(製{造"]
    threads = min(MAX_THREADS, len(sens))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(check_balance, sens)

    with open('new_analysed_text.txt', 'a+', encoding='utf-8') as new_file:
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


lines = []
with open("aozora_sample_text.txt", encoding='utf-8', errors='ignore') as file:
    for line in file:
        if "Title:" not in line:
            lines.append(line.rstrip('\n').replace("―", "").replace("_", "").replace("＼", "")
                         .replace("／", "").replace("＊", "").replace("★", "").replace("』", "")
                         .replace("『", "").replace("●", "").replace("○", "").replace("▲", "")
                         .replace("△", "").replace("┐", "").replace("┌", "").replace("└", "")
                         .replace("┘", "").replace("├", "").replace(" ", ""))

body_text = ''.join(lines).replace("。", "。\n").replace("？", "？\n").replace("?", "?\n") \
    .replace("！", "！\n").replace("!", "!\n").replace("‼", "‼\n").replace("⁉", "⁉\n") \
    .replace("………", "…").replace("……", "…").replace("…", "…\n")
sentences = body_text.split('\n')

seen_set = set()
for filtered_line in sentences:
    print("filtering duplicates")
    if len(filtered_line) >= 6 and filtered_line not in seen_set:
        seen_set.add(filtered_line)

new_seen_set = set()
main(seen_set)
