"""Run doctests in pugnlp.constant"""


import pugnlp.constant

from unittest import TestCase


class T(TestCase):
    """Do-Nothing Test to ensure unittest doesnt ignore this file"""

    def setUp(self):
        pass

    def test_importability(self):
        self.assertTrue(pugnlp.constant)
