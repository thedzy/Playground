# hangman.py

A traditional hangman game.
```
Guessed letters
A   E   I  L NO  RSTU
██████████████████████
██   ▄██▀     █
██ ▄██▀      ▄███▄
████▀       █▀  ▀█
██▀         ▀▄ ▄█▀
██          ▄▄█▀▄
██        ▄█▀██ ▀█
██       ▄█  ██  █
██       ▀▄  █▀ ▄█
██          ▄█▄
██          █▀█▄
██         █▀  █
██         █   █
██         ▀▀  █▄
██

_O_ELESS
POPELESS
You lose
```

## What?

Play a  single player hangman game.

You can use a custom dictionary, word or phrase.\
You can use a custom hangman figure

```bash
usage: hangman.py [-h] [-d DICTIONARY] [-w WORD] [-p PHRASE [PHRASE ...]] [-l LENGTH] [-x LENGTH_MAX] [-m LENGTH_MIN] [--debug]

A traditional hangman game.

optional arguments:
    -h, --help
            show this help message and exit
    -d DICTIONARY, --dict DICTIONARY
            Dictionary file to use
            Default: /Users/syoung/Documents/GitHub/hangman/collins_scrabble_words_2019.txt
    -w WORD, --word WORD
            Word or phrase to use
            Default: Random selection from the dictionary
    -p PHRASE [PHRASE ...], --phrase PHRASE [PHRASE ...]
            Word or phrase to use
            Default: Random word from the dictionary
    -l LENGTH, --length LENGTH
            Only a fixed length word is generated
            Note: Overrides minimum and maximum values
    -x LENGTH_MAX, --max LENGTH_MAX
            Maximum word length generated
            Default: 32
    -m LENGTH_MIN, --min LENGTH_MIN
            Minimum word length generated
            Default: 1
    --debug
            Debug the program
            Default: False
```

## Why?
While, I am sure this has been done to death.  The world can always use another hangman challenge.  No, that's not why.  Partially just looking for a something to code and I wanted to create a proper "hangman" and the challenge of creating and storing that art.

## Improvements?
I think a basic b&w image converter to the stored graphics, maybe online mode.  What can you really do with an early childhood game like this? 3D?

## State?
No known bugs.  Works.
