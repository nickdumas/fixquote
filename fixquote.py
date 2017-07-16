# -*- coding: utf-8 -*-

from string import translate, maketrans

def smartSanitize(s):

    return s.replace("“",'"').replace("”", '"').replace(r"‘",r"'").replace(r"’",r"'").replace("–", "-")

    #badChars = r'“”‘’–'.decode("utf-8")
    #t = maketrans(badChars, r'""''-')
    #return translate(s.decode("utf-8"), t)

if __name__ == "__main__":
    badString = r'“This is a demo quote, with emdash and various other bad characters. –‘Sub quote. ’”'
    sanitized = smartSanitize(badString)
