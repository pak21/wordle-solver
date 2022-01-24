# Wordle Solver

A greedy min-max solver for the now famous
[Wordle](https://www.powerlanguage.co.uk/wordle/); it attempts to minimize the
number of possible answers after each guess. This may not be globally optimal,
but it's probably pretty close and at least shows that a solution does exist.

It does _not_ find a solution for hard mode; my gut feel is that it's not
possible as there are too many sets like `[bchlmpw]atch` which are real "traps"
if you run into them.

## TODO

* Rather than looking at min-max, should we be looking at the entropy (or
similar) of the distribution of possible outcomes after each word?

## Notes

Get word lists from
[here](https://www.reddit.com/r/wordle/comments/s4tcw8/a_note_on_wordles_word_list/hstkip2/);
I have:

```
$ sha1sum wordle-answers-alphabetical.txt wordle-allowed-guesses.txt 
c216eac05a4f78fa749965e9fc8bf2c66c704a8c  wordle-answers-alphabetical.txt
ccf7adfd89f8177d1367224bdb73675f97e9d75b  wordle-allowed-guesses.txt
```
