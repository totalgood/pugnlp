#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tables of data like unicode emojis and extended ASCII translation tables."""
from __future__ import division, print_function, absolute_import, unicode_literals
from builtins import (  # noqa
    bytes, dict, int, list, object, range, str,
    ascii, chr, hex, input, next, oct, open,
    pow, round, super,
    filter, map, zip)

import os
import io

import pandas as pd

from .constants import DATA_PATH

emoticons = []
for cat in ['activities', 'animals-and-nature', 'smilies', 'flags', 'symbols', 'food-and-drink', 'travel-and-places', 'objects']:
    f = io.open(os.path.join(DATA_PATH, 'emojione-' + cat + '.txt'), encoding='utf-8')
    emoticons += [(line.split()[0], ' '.join(line.split()[1:]), cat) for line in f]
emoticon_descriptions = dict((k, (v1, v2)) for k, v1, v2 in emoticons)
description_emoticons = dict(((v1, v2), k) for k, v1, v2 in emoticons)
"""
One of the 1474 unicode emoticons is not unique, even when paired with its category:
>>> len(emoticons)
1474
>>> len(description_emoticons)
1473
>>> len(emoticon_descriptions)
1452
"""


df_extended_ascii = pd.DataFrame.from_csv(os.path.join(DATA_PATH, 'ascii-equivalents.csv'), header=0)
