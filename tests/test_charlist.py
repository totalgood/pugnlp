"""Run doctests in pugnlp.charlist."""
from __future__ import print_function, absolute_import, division, unicode_literals

import pugnlp.charlist

from unittest import TestCase


class Test(TestCase):
    """Basic unit test for the pugnlp.charlist module"""

    def test_importability(self):
        self.assertTrue(pugnlp.charlist)
