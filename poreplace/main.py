#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from optparse import OptionParser
from translate.storage.po import pofile
from pounit import PoUnit
from errata import Errata


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-e', '--errata',
                      action = 'store',
                      type = 'string',
                      dest = 'errata')
    (options, args) = parser.parse_args()
    if not options.errata:
        sys.exit('Oops! Specify your errata: -e <errata>')
    errata = Errata(options.errata)
    input = sys.stdin
    units = pofile.parsefile(input).units
    for unit in units:
        pounit = PoUnit(unit)
        if pounit.istranslated() and \
           not pounit.isobsolete() and \
           not pounit.iscredits():
            pounit.fix_errata(errata.terms)
        print(pounit)
