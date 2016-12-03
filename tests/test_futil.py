"""Run doctests in pugnlp.futil."""
from __future__ import print_function, absolute_import


import pugnlp.futil

from unittest import TestCase


class AllTest(TestCase):
    """Smoke test for the futil (file utilities) module."""
    def test_importability(self):
        self.assertTrue(pugnlp.futil)
