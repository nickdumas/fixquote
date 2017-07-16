# -*- coding: utf-8 -*-

from fixquote import smartSanitize
import unittest

class SmartRemovalTest(unittest.TestCase):
    def test_RmBadChars(self):
        badString = r'“This is a demo quote, with emdash and various other bad characters. –‘Sub quote. ’”'
        expected = '''"This is a demo quote, with emdash and various other bad characters. -'Sub quote. '"'''
        res = smartSanitize(badString)
        self.assertEquals(res, expected)

    def test_NoBadChars(self):
        badString = r'"This is an ordinary string that."'
        expected = r'"This is an ordinary string that."'

        res = smartSanitize(badString)
        self.assertEquals(res, expected)
