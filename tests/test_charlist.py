"""Run doctests in pug_nlp.charlist."""
from __future__ import print_function, absolute_import, division, unicode_literals

import doctest

import pug_nlp.charlist

from unittest import TestCase


class DoNothingTest(TestCase):
    """A useless TestCase to encourage Django unittests to find this module and run `load_tests()`."""
    def test_example(self):
        self.assertTrue(True)


def load_tests(loader, tests, ignore):
    """Run doctests for the pug_nlp.charlist module"""
    tests.addTests(doctest.DocTestSuite(pug_nlp.charlist, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    return tests
