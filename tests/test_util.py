"""Run doctests in pugnlp.futil."""
from __future__ import print_function, absolute_import

import doctest

import pugnlp.futil

from unittest import TestCase


class BasicTest(TestCase):
    """Basic unit test for the pugnlp.charlist module"""

    def test_importability(self):
        self.assertTrue(pugnlp.charlist)


def load_tests(loader, tests, ignore):
    """Run doctests for the pugnlp.stats module"""
    tests.addTests(doctest.DocTestSuite(pugnlp.util, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    return tests
