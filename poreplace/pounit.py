# -*- coding: utf-8 -*-
import re
from translate.misc.multistring import multistring

class PoUnit:
    def __init__(self, unit):
        self.unit = unit

    def __getattr__(self, attr):
        return getattr(self.unit, attr)

    @property
    def target_strings(self):
        return self.target.strings

    def fix_errata(self, terms):
        replaced = False
        newstrings = []
        for string in self.target_strings:
            newstring = self.replace(string, terms)
            if string != newstring:
                string = newstring
                replaced = True
            newstrings.append(string)
        if replaced:
            self.settarget(multistring(newstrings))

    def replace(self, string, terms):
        for term in terms:
            string = term.org.sub(term.new, string)
        return string

    def iscredits(self):
        TRANSLATOR_PATTERN = '^translator[-_]credits$'
        if re.search(TRANSLATOR_PATTERN, self.source):
            return True
        return False

