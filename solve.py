#!/usr/bin/env python3

import argparse
import itertools
from operator import itemgetter

import wordle

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--answers', required=True, help='Answer list')
parser.add_argument('-w', '--words', required=True, help='Word list')
parser.add_argument('--hard', action='store_true', help='Hard mode')
parser.add_argument('-f', '--first', help='Forced first guess')
args = parser.parse_args()

with open(args.answers) as f:
    all_answers = {l.strip() for l in f}

with open(args.words) as f:
    all_words = {l.strip() for l in f}.union(all_answers)

def get_score(answers, guess):
    sigs = [wordle.signature(a, guess) for a in answers]
    return wordle.score(sigs)

def get_next_guess(possibles, words):
    score, next_guess = min([(get_score(possibles, w), w) for w in words])
    return next_guess, score

def recurse(answers, guess, words, hard_mode, depth):
    indent = '  ' * depth
    all_signatures = sorted([(wordle.signature(a, guess), a) for a in answers])
    grouped = itertools.groupby(all_signatures, key=itemgetter(0))

    for sig, p in grouped:
        possibles = [w for _, w in p]
        if len(possibles) == 1:
            if sig == 'ggggg':
                print(f'{indent}{sig}: solution is {possibles[0]} after {depth} guesses')
            else:
                print(f'{indent}{sig}: solution is {possibles[0]} after {depth+1} guesses')
        else:
            filtered_words = words.copy()
            if hard_mode:
                filtered_words = wordle.hard_mode_filter(filtered_words, guess, sig)

            next_guess, score = get_next_guess(possibles, filtered_words)
            print(f'{indent}{sig}: next guess should be {next_guess} with a score of {score}')
            recurse(possibles, next_guess, filtered_words, hard_mode, depth + 1)

if args.first:
    first_guess, score = args.first, '???'
else:
    first_guess, score = get_next_guess(all_answers, all_words)

print(f'First guess should be {first_guess} with a score of {score}')
recurse(all_answers, first_guess, all_words, args.hard, 1)
