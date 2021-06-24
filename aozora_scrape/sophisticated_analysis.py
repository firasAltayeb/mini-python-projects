import time
import concurrent.futures
from allowed_characters import kana_List
from allowed_characters import filtered_kanji
from allowed_characters import latin_characters
from allowed_characters import jlpt_n5_characters
from allowed_characters import jlpt_n4_characters
from allowed_characters import jlpt_n3_characters
from allowed_characters import jlpt_n2_characters
from allowed_characters import jlpt_n1_characters

MAX_THREADS = 10


def jlpt_n5_oriented(sentence):
    for character in sentence:
        if character not in jlpt_n5_characters + kana_List + latin_characters:
            print("above sentence is not n5 oriented")
            return False

    with open('n5_muke_sentences.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")
    return True


def jlpt_n4_oriented(sentence):
    for character in sentence:
        if character not in jlpt_n5_characters + jlpt_n4_characters + kana_List + latin_characters:
            print("above sentence is not n5 oriented")
            return False

    jlpt_n5_oriented(sentence)
    with open('n4_muke_sentences.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")
    return True


def jlpt_n3_oriented(sentence):
    for character in sentence:
        if character not in jlpt_n5_characters + jlpt_n4_characters + jlpt_n3_characters \
                + kana_List + latin_characters:
            print("above sentence is not n5 oriented")
            return False

    jlpt_n4_oriented(sentence)
    with open('n3_muke_sentences.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")
    return True


def jlpt_n2_oriented(sentence):
    for character in sentence:
        if character not in jlpt_n5_characters + jlpt_n4_characters + jlpt_n3_characters \
                + jlpt_n2_characters + kana_List + latin_characters:
            print("above sentence is not n5 oriented")
            return False

    jlpt_n3_oriented(sentence)
    with open('n2_muke_sentences.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")
    return True


def jlpt_n1_oriented(sentence):
    for character in sentence:
        if character not in jlpt_n5_characters + jlpt_n4_characters + jlpt_n3_characters \
                + jlpt_n2_characters + jlpt_n1_characters + kana_List + latin_characters:
            print("above sentence is not n5 oriented")
            return False

    jlpt_n2_oriented(sentence)
    with open('n1_muke_sentences.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")
    return True


def analyse(sentence):
    if not 8 <= len(sentence) <= 30:
        return

    print(sentence)
    for character in sentence:
        if character not in kana_List + filtered_kanji + latin_characters:
            print("{} is out of scope".format(character))
            return False

    jlpt_n1_oriented(sentence)
    with open('full_zora_txt_filtered.txt.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")


def concurrent_run(sens):
    threads = min(MAX_THREADS, len(sens))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(analyse, sens)


def main(sens):
    t0 = time.time()
    concurrent_run(sens)
    t1 = time.time()
    print(f"{t1 - t0} seconds to analyse {len(sens)} stories.")


with open("full_zora_txt_count.txt", encoding='utf-8', errors='ignore') as file:
    lines = [line.rstrip('\n') for line in file]

main(lines)
