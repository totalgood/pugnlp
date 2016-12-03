"""Run doctests in pugnlp.segmentation."""
from __future__ import print_function, absolute_import

import doctest

import pugnlp.segmentation

from unittest import TestCase


class BasicTest(TestCase):
    """Basic unit test for the pugnlp.segmentation module"""

    def test_importability(self):
        self.assertTrue(pugnlp.segmentation)


def load_tests(loader, tests, ignore):
    """Run doctests for the pugnlp.stats module"""
    tests.addTests(doctest.DocTestSuite(pugnlp.segmentation, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    return tests
