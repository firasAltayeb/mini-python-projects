import os
import time
import concurrent.futures
from google.cloud import translate_v2

MAX_THREADS = 10
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\tayeb\Downloads\Miscellaneous\kanjimaster_cloudkey.json"

translate_client = translate_v2.Client()


def translate_text(sentence):
    print('checking ' + sentence)
    result = translate_client.translate(sentence, source_language='ja', target_language='en', format_="text")
    print("Translation: {}".format(result["translatedText"]))

    with open('aozora_translation_pairs.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")
        new_file.write(result['translatedText'] + "\n")


def concurrent_run(sens):
    threads = min(MAX_THREADS, len(sens))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(translate_text, sens)


def main(sens):
    t0 = time.time()
    concurrent_run(sens)
    t1 = time.time()
    print(f"{t1 - t0} seconds to analyse {len(sens)} stories.")


with open("aozora_master_list.txt", encoding='utf-8', errors='ignore') as file:
    lines = [line.rstrip('\n') for line in file]

main(lines)
