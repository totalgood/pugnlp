"""Run doctests in pugnlp.segmentation."""
from __future__ import print_function, absolute_import

import doctest

import pugnlp.segmentation

from unittest import TestCase


class DoNothingTest(TestCase):
    """A useless TestCase to encourage Django unittests to find this module and run `load_tests()`."""
    def test_example(self):
        self.assertTrue(True)


def load_tests(loader, tests, ignore):
    """Run doctests for the pugnlp.segmentation module"""
    tests.addTests(doctest.DocTestSuite(pugnlp.segmentation, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    return tests
