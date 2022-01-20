import pytest

import wordle

class TestSignature():
    def test_same_word(self):
        target = 'robot'
        guess = target

        sig = wordle.signature(target, guess)

        assert sig == 'ggggg'

    def test_no_matches(self):
        target = 'robot'
        guess = 'again'

        sig = wordle.signature(target, guess)

        assert sig == '.....'

    def test_correct_letter_correct_place(self):
        target = 'robot'
        guess = 'relax'

        sig = wordle.signature(target, guess)

        assert sig == 'g....'

    def test_correct_letter_incorrect_place(self):
        target = 'robot'
        guess = 'arise'

        sig = wordle.signature(target, guess)

        assert sig == '.y...'

    def test_duplicated_letter_wrong_place(self):
        target = 'robot'
        guess = 'merry'

        sig = wordle.signature(target, guess)

        assert sig == '..y..'

    def test_duplicated_letter_right_place(self):
        target = 'robot'
        guess = 'stunt'

        sig = wordle.signature(target, guess)

        assert sig == '....g'
