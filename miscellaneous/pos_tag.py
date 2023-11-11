import os
import argparse
import itertools
import random

from collections import Counter, defaultdict
from typing import List
from nltk.metrics.scores import precision, recall, f_measure, accuracy

import numpy as np


# import re

def _divider(line: str) -> bool:
    empty_line = line.strip() == ""
    if empty_line:
        return True
    else:
        return False


def read_conll(conll_input):
    for is_divider, lines in itertools.groupby(conll_input, _divider):
        if not is_divider:
            fields = [line.strip().split() for line in lines]
            fields = [list(field) for field in zip(*fields)]
            tokens, pos_tags, _ = fields

            yield tokens, pos_tags


def kfold_split(sentences: List, fold: int = 10):
    sents_indx = list(range(0, len(sentences)))
    random.shuffle(sents_indx)
    k, m = divmod(len(sents_indx), fold)
    indx_split = [[]] * fold
    for i in range(fold):
        b_idx = i * k + min(i, m)
        e_idx = (i + 1) * k + min(i + 1, m)
        indx_split[i] = sents_indx[b_idx:e_idx]
    return indx_split


def crossval_eval(split_sents: List[List], fold: int = 10):
    for i, fold_th in enumerate(split_sents):
        ts_idx = fold_th
        tr_idx = []
        for tr_ in range(fold):
            if tr_ != i:
                tr_idx.extend(split_sents[tr_])
        yield tr_idx, ts_idx


def train_memorization(train_sents: List, train_tags: List):
    word_tag_dict = {}
    for sent, tags in zip(train_sents, train_tags):
        for word, tag in zip(sent, tags):
            if not (word in word_tag_dict):
                # first word and tag pairs found
                word_tag_dict[word] = Counter({tag: 1})
            else:
                # update word and tag pairs count
                word_tag_dict[word][tag] += 1
    return word_tag_dict


def predict(word: str, word_tag_: dict, common_tag='NN'):
    if word in word_tag_:
        return word_tag_[word].most_common(1)[0][0]
    else:
        return common_tag


def summarize_data(sents_list, index, output_file, delimiter=' '):
    tok_tag_dict = Counter()
    tag_counter = Counter()
    tok_counter = Counter()

    for idx in index:
        sent, pos_tags = sents_list[idx][0], sents_list[idx][1]
        for tok, pos in zip(sent, pos_tags):
            tok_tag_dict[(tok, pos)] += 1
            tag_counter[pos] += 1
            tok_counter[tok] += 1
            print(f'{tok}{delimiter}{pos}', file=output_file)
        print('', file=output_file)

    print(f'sentences : {len(index)}')
    print(f'word types: {len(tok_counter)}')

    for tag, counts in tag_counter.most_common(5):
        print(f'{tag} with counts : {counts}')


def evaluate(sents_list, test, train_dict, output_file, delimiter=' '):
    gold_tags, gold_set = [], []
    pred_tags, pred_set = [], []
    gold_per_tags = defaultdict(int)
    pred_per_tags = defaultdict(int)
    for test_idx in test:
        sent, pos_tags = sents_list[test_idx][0], sents_list[test_idx][1]
        gold_tags.extend(pos_tags)
        for idx, (tok, pos) in enumerate(zip(sent, pos_tags)):
            # predict current token tags using train dictionary
            hyp = predict(tok, train_dict)
            # append the predicted tags for comparison
            pred_tags.append(hyp)
            pred_set.append((tok, hyp, idx, test_idx))
            if pos not in gold_per_tags:
                gold_per_tags[pos] = [(tok, pos, idx, test_idx)]
                if pos not in pred_per_tags:
                    pred_per_tags[pos] = [(tok, hyp, idx, test_idx)]
                elif pos in pred_per_tags:
                    pred_per_tags[pos].append(((tok, hyp, idx, test_idx)))
            elif pos in gold_per_tags:
                gold_per_tags[pos].append((tok, pos, idx, test_idx))
                if pos not in pred_per_tags:
                    pred_per_tags[pos] = [(tok, hyp, idx, test_idx)]
                elif hyp in pred_per_tags:
                    pred_per_tags[pos].append(((tok, hyp, idx, test_idx)))

            gold_set.append((tok, pos, idx, test_idx))

            # out_delim = called_args.output_delimiter
            out_delim = delimiter
            # print the token, gold_tags and predicted_tags into conll formatted file
            # print(f'{tok}{out_delim}{pos}{out_delim}{hyp}')
            line_out = f'{tok}{out_delim}{pos}{out_delim}{hyp}'
            # print(line_out)
            print(line_out, file=output_file)
        print('', file=output_file)

    print(f'accuracy : {accuracy(gold_tags, pred_tags)}')

    gold_set = set(gold_set)
    pred_set = set(pred_set)
    print(f'precision : {precision(gold_set, pred_set)}')
    print(f'recall : {recall(gold_set, pred_set)}')
    print(f'f_measure : {f_measure(gold_set, pred_set)}')

    # per_class = Counter()

    for label, c_gold_set in gold_per_tags.items():
        # print(f'{label}')
        c_gold_set = set(c_gold_set)
        c_pred_set = set(pred_per_tags[label])
        print(f'{label} precision : {precision(c_gold_set, c_pred_set)}')
        print(f'{label} recall : {recall(c_gold_set, c_pred_set)}')
        print(f'{label} f_measure : {f_measure(c_gold_set, c_pred_set)}')


def main(called_args):
    conll_data = open(called_args.conll_input, 'r', encoding='ascii')
    sents_list = list(read_conll(conll_data))
    words_list = np.array([sent[0] for sent in sents_list])
    tags_list = np.array([sent[1] for sent in sents_list])

    split_result = kfold_split(sents_list)

    # for kth, fold in enumerate(split_result):
    for kth, (train, test) in enumerate(crossval_eval(split_result)):
        train_kth_file = open(f'{called_args.output_dir}/train-fold-{kth}.conll', mode='w', encoding='ascii')
        print(f'fold-{kth}')
        print('train')
        summarize_data(sents_list, train, train_kth_file, called_args.output_delimiter)

        train_idx = np.array(train)
        tr_toks_kth = list(words_list[train_idx])
        tr_tags_kth = list(tags_list[train_idx])
        train_dict = train_memorization(tr_toks_kth, tr_tags_kth)

        test_kth_file = open(f'{called_args.output_dir}/test-fold-{kth}.conll', mode='w', encoding='ascii')
        print(f'test')
        summarize_data(sents_list, test, test_kth_file, called_args.output_delimiter)
        test_kth_file.close()
        test_kth_file = open(f'{called_args.output_dir}/test-fold-{kth}.conll', mode='w', encoding='ascii')
        evaluate(sents_list, test, train_dict, test_kth_file, called_args.output_delimiter)

        # print('Confusion matrix:')
        # print(ConfusionMatrix(gold_tags, pred_tags, sort_by_count=True))
        # print(ConfusionMatrix(gold_tags, pred_tags).pretty_format(sort_by_count=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='preprocess conll file to read as data (training and test) in cross-validation',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--conll-input', '--i', help='input filename of conll corpus')
    parser.add_argument('-o', '--output-dir', metavar='DIR', default=os.getcwd(),
                        help='output directory (default: {})'.format(os.getcwd()))
    parser.add_argument('-t', '--input-delimiter', default=' ',
                        help='input sentences delimiter file')
    parser.add_argument('-s', '--sents-delimiter', default='\n',
                        help='input fields delimiter file')
    parser.add_argument('-d', '--output-delimiter', default='\t',
                        help='output delimiter for cross-validation output file')
    parser.add_argument('-e', '--encoding', default='ascii',
                        help='input file encoding and decoding output, default=ascii')
    args = parser.parse_args()
    main(args)
