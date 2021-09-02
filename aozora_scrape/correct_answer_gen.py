import time
from googletrans import Translator

translator = Translator()


def get_correct_translation(sens):
    translations = translator.translate(sens, src='ja', dest='en')

    with open('aozora_master_qna.txt', 'a+', encoding='utf-8') as new_file:
        for translation in translations:
            new_file.write(translation.origin + "\n")
            new_file.write(translation.text + "\n")


def main(sens):
    t0 = time.time()
    get_correct_translation(sens)
    t1 = time.time()
    print(f"{t1 - t0} seconds to analyse {len(sens)} stories.")


with open("aozora_master_list.txt", encoding='utf-8', errors='ignore') as file:
    lines = [line.rstrip('\n') for line in file]

main(lines)
