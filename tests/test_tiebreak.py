import pytest

import wordle

class TestTiebreak():
    def test_prefer_word_in_set(self):
        guess1 = 'build'
        guess2 = 'glade'
        possibles = {guess1, 'guild', 'quill'}

        score1 = wordle.tiebreak(guess1, possibles)
        score2 = wordle.tiebreak(guess2, possibles)

        assert score1 < score2
