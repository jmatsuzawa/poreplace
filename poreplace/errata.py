# -*- coding: utf-8 -*-
import codecs
import os
import re

class Term:
    def __init__(self, org, new):
        self.org = re.compile(unicode(org))
        self.new = unicode(new)

class Errata:
    def __init__(self, fname):
        self.terms = self.parse(fname)

    def parse(self, fname):
        terms = []
        for line in codecs.open(fname, 'r', 'utf_8'):
            org, new = tuple(line.split(','))
            terms.append(Term(org ,new.rstrip()))
        return terms
