"""Run doctests in pugnlp.regex."""
from __future__ import print_function, absolute_import, division, unicode_literals

import doctest

import pugnlp.regex

from unittest import TestCase


class DoNothingTest(TestCase):
    """A useless TestCase to encourage Django unittests to find this module and run `load_tests()`."""
    def test_example(self):
        self.assertTrue(True)


def load_tests(loader, tests, ignore):
    """Run doctests for the pugnlp.regex module"""
    tests.addTests(doctest.DocTestSuite(pugnlp.regex, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    return tests
