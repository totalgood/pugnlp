"""Run doctests in pugnlp.constants"""


import pugnlp.constants

from unittest import TestCase


class Test(TestCase):
    """Basic unit test for the pugnlp.constants module"""

    def setUp(self):
        pass

    def test_importability(self):
        self.assertTrue(pugnlp.constants)
