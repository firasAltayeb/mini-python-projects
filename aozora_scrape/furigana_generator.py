import string
import time

from wanakana import to_hiragana, is_japanese, is_katakana, is_hiragana
from allowed_characters import japanese_punctuation
from sudachipy import dictionary
from sudachipy import tokenizer

tokenizer_obj = dictionary.Dictionary(dict="small").create()

kanji_reading_mapping = {
    '私': '私[わたし]',
    '貴女': '貴女[あなた]',
    '何': '何[なに]',
    '外宇宙': '外宇宙[がいうちゅう]',
    '異星人': '異星人[いせいじん]',
    '優那': '優那[ゆうな]',
    '菜々美': '菜々美[ななみ]'
}

special_character = '〜'


def is_japanese_extended(text):
    return is_japanese(text) and text not in string.punctuation \
           and text not in japanese_punctuation


def to_anki_format(index, kanji, reading):
    return '{}{}[{}]'.format(' ' if index > 0 else '', kanji, reading)


def add_furigana(ja_sentence):
    print("parsing {}".format(ja_sentence))
    tokens = [m for m in tokenizer_obj.tokenize(ja_sentence, tokenizer.Tokenizer.SplitMode.C)]
    parsed = ''
    token_indexes_to_skip = []
    for index, token in enumerate(tokens):
        if index in token_indexes_to_skip:
            continue
        to_parse = is_japanese_extended(token.surface()) and not \
            is_katakana(token.surface()) and not is_hiragana(token.surface())
        if to_parse:
            if token.surface()[-1] in special_character:
                parsed += add_furigana(token.surface()[:-1]) + token.surface()[-1]
            else:
                if index > 0:
                    parsed += ' '
                reading = to_hiragana(token.reading_form())
                if token.surface() in kanji_reading_mapping:
                    parsed += kanji_reading_mapping[token.surface()]
                elif index < len(tokens) - 1 and token.surface() + tokens[index + 1].surface() \
                        in kanji_reading_mapping:
                    parsed += kanji_reading_mapping[tokens[index].surface()
                                                    + tokens[index + 1].surface()]
                    token_indexes_to_skip.append(index + 1)
                else:
                    surface_index = 0
                    reading_index = 0
                    while len(token.surface()) > surface_index:
                        if is_hiragana(token.surface()[surface_index]) or \
                                is_katakana(token.surface()[surface_index]):
                            parsed += token.surface()[surface_index]
                            reading_index += 1
                            surface_index += 1
                        else:
                            next_index = -1
                            for token_index in range(surface_index, len(token.surface())):
                                if is_hiragana(token.surface()[token_index]) or is_katakana(
                                        token.surface()[token_index]):
                                    next_index = token_index
                                    break
                            if next_index < 0:
                                parsed += to_anki_format(
                                    index=surface_index,
                                    kanji=token.surface()[surface_index:], reading=reading[reading_index:])
                                break
                            else:
                                reading_index_tail = reading_index
                                try:
                                    while reading[reading_index_tail] != token.surface()[next_index] or \
                                            (reading_index_tail < len(reading) - 1 and
                                             reading[reading_index_tail] == reading[reading_index_tail + 1]):
                                        reading_index_tail += 1
                                    parsed += to_anki_format(
                                        index=surface_index,
                                        kanji=token.surface()[surface_index:next_index],
                                        reading=reading[reading_index:reading_index_tail])
                                except:
                                    print("omitted {}".format(ja_sentence))
                                    return
                                reading_index = reading_index_tail

                            reading_length = next_index - surface_index
                            if reading_length > 0:
                                surface_index += reading_length
                            else:
                                break
        else:
            parsed += token.surface()
    return parsed


def concurrent_run(sens):
    for j in range(0, len(sens), 2):
        furigana_sentence = add_furigana(sens[j])
        if furigana_sentence is not None:
            with open('temp.txt', 'a+', encoding='utf-8') as new_file:
                new_file.write(furigana_sentence + "\n")
                new_file.write(sens[j + 1] + "\n")


def main():
    with open("second_part.txt", encoding='utf-8', errors='ignore') as file:
        lines = [line.rstrip('\n') for line in file]

    t0 = time.time()
    concurrent_run(lines)
    t1 = time.time()
    print(f"{t1 - t0} seconds to analyse {len(lines)} items.")


main()
