import pytest

import wordle

class TestScore():
    def test_aba(self):
        signatures = ['.....', 'y....', '.....']

        actual = wordle.score(signatures)

        assert actual == 2

    def test_abac(self):
        signatures = ['.....', 'y....', '.....', 'g....']

        actual = wordle.score(signatures)

        assert actual == 2

    def test_abbaa(self):
        signatures = ['.....', 'y....', 'y....', '.....', '.....']

        actual = wordle.score(signatures)

        assert actual == 3
