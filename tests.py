from __future__ import absolute_import, division, unicode_literals

import unittest
import php


class PythonPHPTestCase(unittest.TestCase):
    """Just because something is tested, doesn't mean it is safe"""

    def test_strtotime(self):
        r = php.strtotime("2015-01-01 UTC")
        self.assertEqual(r, 1420070400)

    def test_str_replace(self):
        r = php.str_replace("%body%", "black", "<body text='%body%'>")
        self.assertEqual(r, "<body text='black'>")

    def test_str_replace_list(self):
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        r = php.str_replace(vowels, "", "Hello World of PHP")
        self.assertEqual(r, "Hll Wrld f PHP")

    def test_array_flip(self):
        r = php.array_flip({"foo": "bar", "spam": "eggs"})
        self.assertEqual(r, {"bar": "foo", "eggs": "spam"})

    def test_print_r(self):
        r = php.print_r(['test'])
        self.assertEqual(r, u'Array\n(\n    [0] => test\n)\n')

if __name__ == '__main__':
    unittest.main()
