import concurrent.futures
import time
import re

from allowed_characters import filteredInKanji
from allowed_characters import katakana_characters
from allowed_characters import kana_characters
from allowed_characters import latin_characters
from allowed_characters import jouyou_kanji
from allowed_characters import numerical_digits
from allowed_characters import symbols_n_signs

MAX_THREADS = 10


def filter_sentences(ja_sentence, en_sentence):
    # remove sentences with katakana - only for aozora
    if sum(c in katakana_characters for c in ja_sentence) != 0:
        return False

    # remove sentences with bad delimiting　- only for aozora
    if ja_sentence[0] == "と" or ja_sentence[0] == "が" \
            or ja_sentence[0] == "を":
        return False

    # remove furigana with containing brackets
    ja_sentence = re.sub("[\[].*?[\]]", "", ja_sentence)
    ja_sentence = ja_sentence.replace(" ", "")
    print(ja_sentence)

    # remove characters not taught by Kanji asap
    for character in ja_sentence:
        if character not in kana_characters + latin_characters + jouyou_kanji \
                + filteredInKanji + numerical_digits + symbols_n_signs:
            print("{} is out of scope".format(character))
            return False

    # remove too short or too long
    print('ja sentence len is {}'.format(len(ja_sentence)))
    if not 6 <= len(ja_sentence) <= 32:
        print("sentence length is not appropriate".format(ja_sentence))
        return

    with open('temp.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(ja_sentence + "\n")
        new_file.write(en_sentence + "\n")


def concurrent_run(sens):
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
