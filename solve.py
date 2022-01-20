#!/usr/bin/env python3

import argparse
import functools
import itertools
from operator import itemgetter

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--answers', required=True, help='Answer list')
parser.add_argument('-w', '--words', required=True, help='Word list')
args = parser.parse_args()

with open(args.answers) as f:
    all_answers = {l.strip() for l in f}

with open(args.words) as f:
    words = {l.strip() for l in f}.union(all_answers)

@functools.cache
def signature(possible, guess):
    poss_chars = list(possible)
    sig = ''
    for i, g in enumerate(guess):
        if poss_chars[i] == g:
            poss_chars[i] = None
            sig += 'g'
        else:
            try:
                j = poss_chars.index(g)
                poss_chars[j] = None
                sig += 'y'
            except ValueError:
                sig += '.'

    return sig

def worst_case(answers, guess):
    sigs = sorted([(signature(a, guess), a) for a in answers])
    grouped = itertools.groupby(sigs, key=itemgetter(0))
    return max([len(list(v)) for _, v in grouped])

def get_next_guess(possibles, words):
    potential_guesses = sorted([(worst_case(possibles, w), not(w in possibles), w) for w in words])
    worst_case_count, _, next_guess = potential_guesses[0]
    return next_guess, worst_case_count

def recurse(answers, guess, depth):
    indent = '  ' * depth
    all_signatures = {signature(a, guess) for a in answers}

    for sig in sorted(all_signatures):
        if sig == 'ggggg':
            print(f'{indent}{sig}: {guess} is correct after {depth} guesses')
        else:
            possibles = [a for a in answers if signature(a, guess) == sig]
            next_guess, worst_case_count = get_next_guess(possibles, words)
            print(f'{indent}{sig}: next guess should be {next_guess} which leaves a worst case of {worst_case_count}')
            recurse(possibles, next_guess, depth + 1)

if True:
    first_guess, worst_case_count = get_next_guess(all_answers, words)
    print(f'First guess should be {first_guess} which leaves a worst case of {worst_case_count}')
    recurse(all_answers, first_guess, 1)
else:
    recurse(all_answers, 'raise', 1)
