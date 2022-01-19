#!/usr/bin/env python3

import argparse
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

def signature1(i, g, possible):
    return 'g' if possible[i] == g else ('y' if g in possible else '.')

def signature(possible, guess):
    return ''.join([signature1(i, g, possible) for i, g in enumerate(guess)])

def worst_case(answers, guess):
    sigs = sorted([(signature(a, guess), a) for a in answers])
    grouped = itertools.groupby(sigs, key=itemgetter(0))
    n = max([len(list(v)) for _, v in grouped])
    return n

def recurse(answers, guess, depth):
    indent = '  ' * depth
    all_signatures = {signature(a, guess) for a in answers}

    for sig in sorted(all_signatures):
        possibles = [a for a in answers if signature(a, guess) == sig]

        if len(possibles) == 1:
            print(f'{indent}{sig}: only possible answer is {possibles[0]}')
        else:
            potential_guesses = sorted([(worst_case(possibles, w), w) for w in all_answers])
            grouped = itertools.groupby(potential_guesses, key=itemgetter(0))
            worst_case_count, best_guesses_g = next(iter(grouped))
            best_guesses = {g[1] for g in best_guesses_g}
            overlap = best_guesses.intersection(possibles)
            next_guess = list(overlap)[0] if overlap else list(best_guesses)[0]
            print(f'{indent}{sig}: next guess should be {next_guess} which leaves a worst case of {worst_case_count}')
            recurse(possibles, next_guess, depth + 1)

if True:
    potential_guesses = sorted([(worst_case(all_answers, w), w) for w in all_answers])
    worst_case_count, first_guess = potential_guesses[0]
    print(f'First guess should be {first_guess} which leaves a worst case of {worst_case_count}')
    recurse(all_answers, first_guess, 1)
else:
    recurse(all_answers, 'raise', 0)
