# -*- coding: utf-8 -*-
import unittest
import sys
import os
from pounit import PoUnit

class TestPoUnit(unittest.TestCase):
    def setUp(self):
        pass

    def test_fix_errata(self):
        errata = [self.make_term(u'フォルダ(?!ー),フォルダー')]
        pounit = self.make_pounit(
            u'''msgid "folder"
                msgstr "フォルダ"
            ''')
        pounit.fix_errata(errata)
        self.assertEqual(pounit.target, u'フォルダー')

    def test_fix_errata_split(self):
        errata = [self.make_term(u'フォルダ(?!ー),フォルダー')]
        pounit = self.make_pounit(
            u'''msgid "folder"
                msgstr "フォ"
                "ルダ"
            ''')
        pounit.fix_errata(errata)
        self.assertEqual(pounit.target, u'フォルダー')

    def test_fix_errata_multi_part(self):
        errata = [self.make_term(u'フォルダ(?!ー),フォルダー')]
        pounit = self.make_pounit(
            u'''msgid "folder/home folder"
                msgstr "フォルダ/ホームフォルダ"
            ''')
        pounit.fix_errata(errata)
        self.assertEqual(pounit.target, u'フォルダー/ホームフォルダー')

    def test_fix_errata_nplurals1(self):
        errata = [self.make_term(u'フォルダ(?!ー),フォルダー')]
        pounit = self.make_pounit(
            u'''msgid "folder"
                msgid_plural "folders"
                msgstr[0] "フォルダ"
            ''')
        pounit.fix_errata(errata)
        self.assertEqual(pounit.target, u'フォルダー')

    def test_fix_errata_nplurals2(self):
        errata = [self.make_term(u'フォルダ(?!ー),フォルダー')]
        pounit = self.make_pounit(
            u'''msgid "folder"
                msgid_plural "folders"
                msgstr[0] "0 フォルダ"
                msgstr[1] "1 フォルダ"
            ''')
        pounit.fix_errata(errata)
        self.assertEqual(pounit.target_strings[0], u'0 フォルダー')
        self.assertEqual(pounit.target_strings[1], u'1 フォルダー')

    def test_fix_errata_not(self):
        errata = [self.make_term(u'フォルダ(?!ー),フォルダー')]
        pounit = self.make_pounit(
            u'''msgid "folder"
                msgstr "フォルダー"
            ''')
        pounit.fix_errata(errata)
        self.assertEqual(pounit.target, u'フォルダー')

    ##############
    # helper
    ##############
    def make_term(self, src):
        import errata
        org, new = tuple(src.split(','))
        return errata.Term(org ,new.rstrip())

    def make_pounit(self, src):
        from translate.storage.po import pofile
        po = self.make_po(src)
        return PoUnit(pofile.parsefile(po).units[0])

    def make_po(self, src):
        import StringIO
        import re
        data = re.sub('^\s*', '', src.encode('utf-8'), flags=re.MULTILINE)
        return StringIO.StringIO(data)


if __name__ == '__main__':
    unittest.main()
