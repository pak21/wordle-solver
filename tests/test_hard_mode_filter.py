import pytest

import wordle

class TestHardModeFilter():
    def test_all_incorrect_filter(self):
        words = {'again', 'relax', 'arise', 'merry', 'stunt'}
        guess = 'robot'
        signature = '.....'

        actual = wordle.hard_mode_filter(words, guess, signature)

        assert actual == words

    def test_correct_letter_correct_place(self):
        words = {'again', 'relax', 'arise', 'merry', 'stunt'}
        guess = 'robot'
        signature = 'g....'

        expected = {'relax'}

        actual = wordle.hard_mode_filter(words, guess, signature)

    def test_correct_letter_incorrect_place(self):
        words = {'again', 'relax', 'arise', 'merry', 'stunt'}
        guess = 'robot'
        signature = 'y....'

        expected = {'arise', 'merry'}

        actual = wordle.hard_mode_filter(words, guess, signature)

    def test_yg_gg(self):
        words = {'dowdy', 'goody', 'howdy', 'moody', 'toddy', 'woody'}
        guess = 'woody'
        signature = 'yg.gg'

        expected = {'dowdy', 'howdy'}

        actual = wordle.hard_mode_filter(words, guess, signature)

        assert actual == expected

    def test_duplicated_letter(self):
        words = {'soily'}
        guess = 'llama'
        signature = 'yy...'

        expected = set()

        actual = wordle.hard_mode_filter(words, guess, signature)

        assert actual == expected
