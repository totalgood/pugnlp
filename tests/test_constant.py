"""Run doctests in pugnlp.constant"""


import pugnlp.constant

from unittest import TestCase


class Test(TestCase):
    """Basic unit test for the pugnlp.constant module"""

    def setUp(self):
        pass

    def test_importability(self):
        self.assertTrue(pugnlp.constant)
