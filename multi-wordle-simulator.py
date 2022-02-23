#!/usr/bin/env python3

import argparse
import functools
import random

import wordle

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--answers', required=True, help='Answer list')
parser.add_argument('-w', '--words', required=True, help='Word list')
parser.add_argument('-g', '--guess', required=True, help='First guess')
parser.add_argument('-n', '--puzzles', required=True, type=int, help='Number of simultaneous puzzles')
args = parser.parse_args()

with open(args.answers) as f:
    all_answers = {l.strip() for l in f}

with open(args.words) as f:
    all_words = {l.strip() for l in f}.union(all_answers)

def get_score(answers, guess):
    sigs = [wordle.signature(a, guess) for a in answers]
    return wordle.score(sigs)

possibles = [all_answers.copy() for i in range(args.puzzles)]

answers = random.sample(list(all_answers), args.puzzles)
print(f'Answers are {answers}')

guess = args.guess
guesses = 1

while True:
    print(f'Guess {guesses}')
    for i in range(args.puzzles):
        if possibles[i]:
            sig = wordle.signature(answers[i], guess)
            print(f'  Signature for puzzle {i+1} is {sig}')
            possibles[i] = [w for w in possibles[i] if wordle.signature(w, guess) == sig]

    possible_counts = [len(x) for x in possibles]
    print(f'  Possible counts: {possible_counts}')

    for i, p in enumerate(possibles):
        if possible_counts[i] > 0 and possible_counts[i] <= 11:
            print(f'  Possible words for puzzle {i+1}: {possibles[i]}')

    try:
        known = possible_counts.index(1)
        guess = list(possibles[known])[0]
        print(f'  Next guess should be "{guess}" to solve puzzle {known+1}')
        possibles[known] = set()
    except ValueError:
        if sum(possible_counts) <= 0:
            raise Exception('All done!')

        entropies = [
          {w: get_score(ps, w) for w in all_words}
          for ps
          in possibles
        ]
        entropy_sum = functools.reduce(lambda a, b: {w: a[w] + b[w] for w in a}, entropies)
        combined = sorted([(v, k) for k, v in entropy_sum.items()])
        _, guess = min(combined)
        print()
        print(combined[:10])
        print(f'  Next guess should be "{guess}"')
    
    print()
    guesses += 1
