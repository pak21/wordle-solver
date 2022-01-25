import pytest

import wordle

class TestScore():
    def test_prefer_even_distribution(self):
        good = ['g....', 'y....'] * 5
        bad = ['.....'] * 10

        good_score = wordle.score(good)
        bad_score = wordle.score(bad)

        assert good_score < bad_score

    def test_prefer_wide_distribution(self):
        good = ([0] * 50) + list(range(1, 51))
        bad = ([0] * 49) + ([1] * 49) + [2, 3]

        good_score = wordle.score(good)
        bad_score = wordle.score(bad)

        assert good_score < bad_score

    def test_prefer_exact_match(self):
        good = ['ggggg', 'y....', 'g....']
        bad = ['.....', 'y....', 'g....']

        good_score = wordle.score(good)
        bad_score = wordle.score(bad)

        assert good_score < bad_score
