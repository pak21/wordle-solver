import pytest

import wordle

class TestScore():
    def test_prefer_word_in_set(self):
        guess1 = 'build'
        guess2 = 'glade'
        possibles = {guess1, 'guild', 'quill'}

        score1 = wordle.score(guess1, possibles)
        score2 = wordle.score(guess2, possibles)

        assert score1 < score2
