#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sentence and token/word segmentation utilities like Tokenizer"""
from __future__ import division, print_function, absolute_import  # , unicode_literals
from future import standard_library
standard_library.install_aliases()  # noqa
from builtins import (  # noqa
    bytes, dict, int, list, object, range, str, ascii, chr, hex, input, next, oct, open,
    pow, round, super, filter, map, zip)
from past.builtins import basestring

import os
import re
from itertools import chain
import logging

from .detector_morse import Detector
from .detector_morse import slurp
from .futil import find_files
from .constants import DATA_PATH
from .futil import generate_files
from .segmentation import *  # noqa

# from .penn_treebank_tokenizer import word_tokenize

logger = logging.getLogger(__name__)
try:
    from nlup import BinaryAveragedPerceptron
except ImportError:
    logger.error("detector_morse disabled because Kyle Gorman's nlup sentence boundary detector has not been installed.")

    class BinaryAveragedPerceptron:
        pass

# TODO: break this up


def generate_sentences(text='', train_path=None, case_sensitive=True, ext=['.md', '.txt', '.asc', '.asciidoc'],
                       normalize_ordinals=1, normalize_newlines=1, normalize_sentence_boundaries=1,
                       epochs=20, classifier=BinaryAveragedPerceptron,
                       re_eol=r'\r\n|\r|\n', **kwargs):
    """Generate sentences from a sequence of characters (text)

    Wrapped text (newlines at column 80, for instance) will break this, breaking up sentences.
    Wrapper and preprocessor for Kyle Gorman's "DetectorMorse" module

    Arguments:
      preprocess (bool): whether to assume common sentence delimitters in markdown and asciidoc formatting
                         using r'[.?!][ \t]*\n\n|[.?!][ \t]*\r\n\r\n|[.?!][ \t]*\r\r|[.?!][ ][ ][A-Z]'
      case_sensitive (int): whether to consider case to make decisions about sentence boundaries
      epochs (int): number of epochs (iterations for classifier training)

    """
    ext = [ext] if isinstance(ext, basestring) else ext
    if isinstance(text, basestring) and len(text) <= 256:
        if os.path.isfile(text) and os.path.splitext(text)[-1].lower() in ext:
            text = open(text)
        elif os.path.isdir(text):
            return chain.from_iterable((
                generate_sentences(text=stat['path'], train_path=train_path, ext=ext,
                                   normalize_ordinals=normalize_ordinals, normalize_newlines=normalize_ordinals,
                                   normalize_sentence_boundaries=normalize_sentence_boundaries,
                                   epochs=epochs, classifier=classifier, re_eol=re_eol, **kwargs)
                for stat in find_files(text, ext=ext)))
    if isinstance(text, basestring):
        texts = Split(text=text, re_delim=re_eol)
    else:
        texts = chain.from_iterable(Split(text=doc, re_delm=re_eol) for doc in text)

    if normalize_newlines:
        re_eol = re.compile(r'\r\n|\r')
        texts = (re_eol.sub(r'\n', doc) for doc in texts)
    if normalize_ordinals:
        re_ord = re.compile(r'\b([0-9]+|[A-Za-z])[.?!][ \t]{1,4}([A-Za-z])')
        texts = (re_ord.sub(r'\1) \2', doc) for doc in texts)
    if normalize_sentence_boundaries:
        re_eos = re.compile(r'([.?!])([ ][ ])[\n]?([A-Z])')
        texts = (re_eos.sub(r'\1\n\3', doc) for doc in texts)

    if train_path:
        generate_sentences.detector = Detector(slurp(train_path), epochs=epochs, nocase=not case_sensitive)
    elif not isinstance(getattr(generate_sentences, 'detector', None), Detector):
        generate_sentences.detector = Detector.load(
            os.path.join(DATA_PATH, 'wsj_pugnlp.detector_morse.Detector.json.gz'))
    # generate_sentences.detector = SentenceDetector(text=text, nocase=not case_sensitive,
    # epochs=epochs, classifier=classifier)
    return iter(chain.from_iterable((s.lstrip() for s in generate_sentences.detector.segments(text)) for text in texts))


class PassageIter(object):

    """Passage (document, sentence, line, phrase) generator for files at indicated path

    Walks all the text files it finds in the indicated path,
    segmenting sentences and yielding them one at a time

    References:
      Radim's [word2vec tutorial](http://radimrehurek.com/2014/02/word2vec-tutorial/)
    """

    def __init__(self, path='', ext='', level=None, dirs=False, files=True,
                 sentence_segmenter=generate_sentences, word_segmenter=str.split, verbosity=0):
        self.file_generator = generate_files(path=path, ext='', level=None, dirs=False, files=True, verbosity=0)

    def __iter__(self):
        for fname in os.listdir(self.file_generator):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
