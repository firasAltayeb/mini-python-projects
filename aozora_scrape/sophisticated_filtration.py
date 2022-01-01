import concurrent.futures
import time

from allowed_characters import filteredInKanji
from allowed_characters import katakana_characters
from allowed_characters import jlpt_n1_characters
from allowed_characters import jlpt_n2_characters
from allowed_characters import jlpt_n3_characters
from allowed_characters import jlpt_n4_characters
from allowed_characters import jlpt_n5_characters
from allowed_characters import kana_characters
from allowed_characters import latin_characters
from allowed_characters import jouyou_kanji
from allowed_characters import numerical_digits
from allowed_characters import symbols_n_signs

MAX_THREADS = 10


def jlpt_n5_oriented(sentence):
    for character in sentence:
        if character not in jlpt_n5_characters + kana_characters + latin_characters \
                + numerical_digits + symbols_n_signs:
            print("above sentence is not n5 oriented")
            return False

    with open('n5_muke_sentences.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")


def jlpt_n4_oriented(sentence):
    for character in sentence:
        if character not in jlpt_n5_characters + jlpt_n4_characters + kana_characters \
                + latin_characters + numerical_digits + symbols_n_signs:
            print("above sentence is not n5 oriented")
            return False

    jlpt_n5_oriented(sentence)
    with open('n4_muke_sentences.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")


def jlpt_n3_oriented(sentence):
    for character in sentence:
        if character not in jlpt_n5_characters + jlpt_n4_characters + jlpt_n3_characters \
                + kana_characters + latin_characters + numerical_digits + symbols_n_signs:
            print("above sentence is not n5 oriented")
            return False

    jlpt_n4_oriented(sentence)
    with open('n3_muke_sentences.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")


def jlpt_n2_oriented(sentence):
    for character in sentence:
        if character not in jlpt_n5_characters + jlpt_n4_characters + jlpt_n3_characters \
                + jlpt_n2_characters + kana_characters + latin_characters \
                + numerical_digits + symbols_n_signs:
            print("above sentence is not n5 oriented")
            return False

    jlpt_n3_oriented(sentence)
    with open('n2_muke_sentences.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")


def jlpt_n1_oriented(sentence):
    for character in sentence:
        if character not in jlpt_n5_characters + jlpt_n4_characters + jlpt_n3_characters \
                + jlpt_n2_characters + jlpt_n1_characters + kana_characters \
                + latin_characters + numerical_digits + symbols_n_signs:
            print("above sentence is not n5 oriented")
            return False

    jlpt_n2_oriented(sentence)
    with open('n1_muke_sentences.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")


def filter_sentences(ja_sentence, en_sentence):
    print(ja_sentence)
    number_of_chara = 0
    open_bracket_found = False

    # # remove sentences with katakana - only for aozora
    if sum(c in katakana_characters for c in ja_sentence) != 0:
        return False

    # # remove sentences starting with particles
    if ja_sentence[0] == "と" or ja_sentence[0] == "が":
        return False

    # remove characters not taught by Kanji asap
    for character in ja_sentence:
        if character not in kana_characters + latin_characters + jouyou_kanji \
                + jlpt_n1_characters + numerical_digits + symbols_n_signs:
            print("{} is out of scope".format(character))
            return False
        # if true, stop counting (for furigana)
        if character == '（':
            open_bracket_found = True
        # only counting kana to avoid kanji-full sentences
        if not open_bracket_found and character in kana_characters:
            number_of_chara += 1
        # if true, start counting again (for furigana)
        if character == '）':
            open_bracket_found = False

    # remove too short or too long
    if not 5 <= number_of_chara <= 30:
        print("{} - is too short or long".format(ja_sentence))
        return

    # jlpt_n1_oriented(ja_sentence)

    with open('aozora_translation_filtered_new.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(ja_sentence + "\n")
        new_file.write(en_sentence + "\n")


def concurrent_run(sens):
    print("filtering characters")
    for j in range(0, len(sens), 2):
        filter_sentences(sens[j], sens[j + 1])
    # threads = min(MAX_THREADS, len(sens))
    # with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
    #     executor.map(filter_sentences, sens)


def main():
    with open("aozora_translation_pairs.txt", encoding='utf-8', errors='ignore') as file:
        lines = [line.rstrip('\n') for line in file]

    seen_list = []
    # check if sentences contain at least one relevant kanji
    # step with 2 to avoid scanning en translations
    for i in range(0, len(lines), 2):
        if sum(c in filteredInKanji for c in lines[i]) == 0:
            continue
        if lines[i] not in seen_list:
            print("not seen {}".format(lines[i]))
            seen_list.append(lines[i])
            seen_list.append(lines[i + 1])

    t0 = time.time()
    concurrent_run(seen_list)
    t1 = time.time()
    print(f"{t1 - t0} seconds to analyse {len(seen_list)} items.")


main()
