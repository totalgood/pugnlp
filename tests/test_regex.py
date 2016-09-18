"""Run doctests in pug_nlp.regex."""
from __future__ import print_function, absolute_import, division, unicode_literals

import doctest

import pug_nlp.regex

from unittest import TestCase


class DoNothingTest(TestCase):
    """A useless TestCase to encourage Django unittests to find this module and run `load_tests()`."""
    def test_example(self):
        self.assertTrue(True)


def load_tests(loader, tests, ignore):
    """Run doctests for the pug_nlp.regex module"""
    tests.addTests(doctest.DocTestSuite(pug_nlp.regex, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    return tests
