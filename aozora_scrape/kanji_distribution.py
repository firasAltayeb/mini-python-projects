import time
import concurrent.futures
from allowed_characters import filtered_kanji

MAX_THREADS = 10
kanji_dic = {kanji[1]: 0 for kanji in enumerate(filtered_kanji)}


def check_occurrence(sentence):
    print('checking ' + sentence)
    global kanji_dic
    for key, value in kanji_dic.items():
        if key in sentence:
            kanji_dic[key] = value + 1


def concurrent_run(sens):
    threads = min(MAX_THREADS, len(sens))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(check_occurrence, sens)

    for key, value in kanji_dic.items():
        print(key, ' : ', value, file=open('master_distribution.txt', 'a+', encoding='utf-8'))


def main(sens):
    t0 = time.time()
    concurrent_run(sens)
    t1 = time.time()
    print(f"{t1 - t0} seconds to analyse {len(sens)} stories.")


with open("aozora_master_list.txt", encoding='utf-8', errors='ignore') as file:
    lines = [line.rstrip('\n') for line in file]

main(lines)
