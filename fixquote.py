# -*- coding: utf-8 -*-

from string import translate, maketrans

BAD_CHARS = [('“', '"'),
             ('”', '"'),
             ("‘", "'"),
             ("’", "'"),
             ("–", "-")]

def smartSanitize(s, badChars=BAD_CHARS):
    '''
    smartSanitize replaces characters in a string.

    s: input string; can be any encoding but must match encoding of strings in badChars
    badChars: a sequence of 2-tuples of the form `( badCharacter, goodCharacter )`. badCharacter is replaced by goodCharacter
    '''
    res = s
    for bad,good in BAD_CHARS:
        res = res.replace(bad, good)

    return res

if __name__ == "__main__":
    badString = r'“This is a demo quote, with emdash and various other bad characters. –‘Sub quote. ’”'
    sanitized = smartSanitize(badString)
