import time
import concurrent.futures
from allowed_characters import kana_List
from allowed_characters import filtered_kanji
from allowed_characters import latin_characters

MAX_THREADS = 10


def analyse(sentence):
    include_sentence = True
    print(sentence)
    for character in sentence:
        if character not in kana_List:
            print("{} is not included".format(character))
            include_sentence = False
        elif character not in filtered_kanji:
            print("{} is not included".format(character))
            include_sentence = False
        elif character not in latin_characters:
            print("{} is not included".format(character))
            include_sentence = False

    if include_sentence:
        print("contained")
        with open('short_text_analysed.txt', 'a+', encoding='utf-8') as new_file:
            new_file.write(sentence + "\n")


def concurrent_run(card_links):
    threads = min(MAX_THREADS, len(card_links))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(analyse, card_links)


def main(sens):
    t0 = time.time()
    concurrent_run(sens)
    t1 = time.time()
    print(f"{t1 - t0} seconds to analyse {len(sens)} stories.")


with open("short_aozora_text.txt", encoding='utf-8', errors='ignore') as file:
    lines = [line.rstrip('\n') for line in file]

main(lines)
