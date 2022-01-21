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

def score(guess, possibles):
    return (not(guess in possibles), -sum([sum([a == b for a, b in zip(guess, w)]) for w in possibles]))
