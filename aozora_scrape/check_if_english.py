import time
import json
import string

with open('english_dictionary.json', 'r') as JSON:
    json_dict = json.load(JSON)


def check_occurrence(ja_sentence, en_sentence):
    print('checking ' + en_sentence)
    punctuation_less = en_sentence.translate(str.maketrans('', '', string.punctuation))
    if any(word.lower() not in json_dict for word in punctuation_less.split()):
        return False
    print('passed check')
    with open('temp.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(ja_sentence + "\n")
        new_file.write(en_sentence + "\n")


def concurrent_run(sens):
    for j in range(1, len(sens), 2):
        check_occurrence(sens[j - 1], sens[j])


def main():
    with open("tanaka_corpus_filtered.txt", encoding='utf-8', errors='ignore') as file:
        lines = [line.rstrip('\n') for line in file]

    t0 = time.time()
    concurrent_run(lines)
    t1 = time.time()
    print(f"{t1 - t0} seconds to analyse {len(lines)} stories.")


main()
