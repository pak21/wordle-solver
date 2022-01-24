import collections
import functools

@functools.cache
def signature(target, guess):
    target_chars = list(target)
    guess_chars = list(guess)
    sig = ['.'] * 5

    # Match letters in the correct place first
    for i in range(len(guess_chars)):
        if target_chars[i] == guess_chars[i]:
            target_chars[i] = None
            guess_chars[i] = None
            sig[i] = 'g'

    # Now match letters in the wrong place, biasing left
    for i, g in enumerate(guess_chars):
        try:
            if g:
                j = target_chars.index(g)
                target_chars[j] = None
                sig[i] = 'y'
        except ValueError:
            pass

    return ''.join(sig)

def score(signatures):
    return max(collections.Counter(signatures).values())

def tiebreak(guess, possibles):
    return (not(guess in possibles), -sum([sum([a == b for a, b in zip(guess, w)]) for w in possibles]))

def _incorrect_place_filter(word, required):
    word_letters = collections.Counter(word)
    for requirement_letter, requirement_count in required.items():
        if word_letters.get(requirement_letter, 0) < requirement_count:
            return False

    return True

def hard_mode_filter(words, guess, signature):
    correct_place_matches = [(i, g) for i, (g, s) in enumerate(zip(guess, signature)) if s == 'g']
    for i, g in correct_place_matches:
        words = {w for w in words if w[i] == g}

    incorrect_place_matches = collections.Counter([g for g, s in zip(guess, signature) if s != '.'])
    words = {w for w in words if _incorrect_place_filter(w, incorrect_place_matches)}

    return words
