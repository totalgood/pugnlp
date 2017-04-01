"""Run doctests in pugnlp.regexes."""
from __future__ import print_function, absolute_import, division, unicode_literals

import pugnlp.regexes

from unittest import TestCase


class BasicTest(TestCase):
    """Basic unit test for the pugnlp.regexes module"""

    def test_importability(self):
        self.assertTrue(pugnlp.regexes)
