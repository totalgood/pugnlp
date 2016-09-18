"""Run doctests in pugnlp.constant"""

import doctest

import pugnlp.constant

from unittest import TestCase


class T(TestCase):
    """Do-Nothing Test to ensure unittest doesnt ignore this file"""

    def setUp(self):
        pass

    def test_doctests(self):
        self.assertEqual(doctest.testmod(pugnlp.constant, verbose=True).failed, 0)


def load_tests(loader, tests, ignore):
    """Run doctests for the clayton.nlp module"""
    tests.addTests(doctest.DocTestSuite(pugnlp.constant, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    return tests
