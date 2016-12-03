#!/usr/bin/env python
"""
Uses the python unittest module to test this app with `python -m unittest pugnlp`.
"""
from __future__ import division, print_function, absolute_import, unicode_literals
# from future import standard_library
# standard_library.install_aliases()  # noqa

import sys
# from django.test import TestCase
from unittest import TestCase
import doctest
import pugnlp as nlp
# from pugnlp import util  # , http, charlist, regex, penn_treebank_tokenizer, detector_morse


class DocTest(TestCase):
    """Doesn't display information about failed tests so not as useful as individual test_module.py doctest runners"""

    # def module_doctester(self, module=None):
    #     if module:
    #         failure_count, test_count = doctest.testmod(
    #             module, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE, raise_on_error=False, verbose=True)
    #         msg = "Ran {0} tests in {3} and {1} passed ({2} failed)".format(test_count, test_count-failure_count, failure_count, module.__file__)
    #         print(msg)
    #         if failure_count:
    #             # print "Ignoring {0} doctest failures...".format(__file__)
    #             self.fail(msg)
    #         # return failure_count, test_count

    def test_importability(self):
        self.assertTrue(nlp)


def load_tests(loader, tests, ignore):
    """Run doctests for the clayton.nlp module"""

    # doctests only verified on Python >= 3.5
    if (sys.version_info >= (3, 5)):
        print('Running doctests for version {}'.format(sys.version_info))
        for name in nlp.__all__:
            tests.addTests(doctest.DocTestSuite(getattr(nlp, name),
                           optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    else:
        print('NOT running doctests for version {}'.format(sys.version_info))
    return tests
