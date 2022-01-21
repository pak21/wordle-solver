#!/usr/bin/env python3

import argparse
import collections
import itertools
from operator import itemgetter

import wordle

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--answers', required=True, help='Answer list')
parser.add_argument('-w', '--words', required=True, help='Word list')
args = parser.parse_args()

with open(args.answers) as f:
    all_answers = {l.strip() for l in f}

with open(args.words) as f:
    words = {l.strip() for l in f}.union(all_answers)

def worst_case(answers, guess):
    sigs = [wordle.signature(a, guess) for a in answers]
    return max(collections.Counter(sigs).values())

def get_next_guess(possibles, words):
    potential_guesses = [(worst_case(possibles, w), not(w in possibles), w) for w in words]
    worst_case_count, _, next_guess = min(potential_guesses)
    return next_guess, worst_case_count

def recurse(answers, guess, depth):
    indent = '  ' * depth
    all_signatures = sorted([(wordle.signature(a, guess), a) for a in answers])
    grouped = itertools.groupby(all_signatures, key=itemgetter(0))

    for sig, p in grouped:
        possibles = [w for _, w in p]
        if sig == 'ggggg':
            print(f'{indent}{sig}: {guess} is correct after {depth} guesses')
        else:
            next_guess, worst_case_count = get_next_guess(possibles, words)
            print(f'{indent}{sig}: next guess should be {next_guess} which leaves a worst case of {worst_case_count}')
            recurse(possibles, next_guess, depth + 1)

first_guess, worst_case_count = get_next_guess(all_answers, words)
print(f'First guess should be {first_guess} which leaves a worst case of {worst_case_count}')
recurse(all_answers, first_guess, 1)
