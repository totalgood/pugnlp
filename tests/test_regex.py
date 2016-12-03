"""Run doctests in pugnlp.regex."""
from __future__ import print_function, absolute_import, division, unicode_literals

import pugnlp.regex

from unittest import TestCase


class BasicTest(TestCase):
    """Basic unit test for the pugnlp.regex module"""

    def test_importability(self):
        self.assertTrue(pugnlp.regex)
