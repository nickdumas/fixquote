# -*- coding: utf-8 -*-

from string import translate, maketrans

BAD_CHARS = [('“', '"'),
             ('”', '"'),
             ("‘", "'"),
             ("’", "'"),
             ("–", "-")]

def smartSanitize(s, badChars=BAD_CHARS):
    res = s
    for bad,good in BAD_CHARS:
        res = res.replace(bad, good)

    return res

if __name__ == "__main__":
    badString = r'“This is a demo quote, with emdash and various other bad characters. –‘Sub quote. ’”'
    sanitized = smartSanitize(badString)
