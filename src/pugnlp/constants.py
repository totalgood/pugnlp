#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Constants and discovered values, like path to current installation of pug-nlp."""
from __future__ import print_function, unicode_literals, division, absolute_import
from future import standard_library
standard_library.install_aliases()  # noqa
from builtins import *  # noqa

from future.utils import viewitems  # noqa
from past.builtins import basestring  # noqa

import os
import string
import datetime
from pytz import timezone
from collections import Mapping, OrderedDict

import pandas as pd

from decimal import Decimal

# TZ constants
try:
    from django.conf import settings
    TIME_ZONE = timezone(settings.TIME_ZONE)
except:
    TIME_ZONE = timezone('UTC')
DEFAULT_TZ = timezone('UTC')

BASE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_PATH, 'data')

ROUNDABLE_NUMERIC_TYPES = (float, int, Decimal, bool)
FLOATABLE_NUMERIC_TYPES = (float, int, Decimal, bool)
BASIC_NUMERIC_TYPES = (float, int)
NUMERIC_TYPES = (float, int, Decimal, complex, str)  # datetime.datetime, datetime.date
NUMBERS_AND_DATETIMES = (float, int, Decimal, complex, str)
SCALAR_TYPES = (float, int, Decimal, bool, complex, str)  # datetime.datetime, datetime.date
# numpy types are derived from these so no need to include numpy.float64, numpy.int64 etc
DICTABLE_TYPES = (Mapping, tuple, list)  # convertable to a dictionary (inherits Mapping or is a list of key/value pairs)
VECTOR_TYPES = (list, tuple)
PUNC = str(string.punctuation)

# synonyms for "count"
COUNT_NAMES = ['count', 'cnt', 'number', 'num', '#', 'frequency', 'probability', 'prob', 'occurences']
# 4 types of "histograms" and their canonical name/label
HIST_NAME = {
    'hist': 'hist',  'ff': 'hist',  'fd': 'hist', 'dff':  'hist', 'dfd': 'hist', 'gfd': 'hist', 'gff': 'hist', 'bfd': 'hist', 'bff': 'hist', # noqa
    'pmf':  'pmf',  'pdf': 'pmf',   'pd': 'pmf',  # noqa  prob. mass/density function, prob. density
    'cmf':  'cmf',  'cdf': 'cmf',  # noqa
    'cfd':  'cfd',  'cff': 'cfd',   'cdf': 'cfd',  # noqa
}
HIST_CONFIG = {
    'hist': {
        'name': 'Histogram',  # frequency distribution, frequency function, discrete ff/fd, grouped ff/fd, binned ff/fd
        'kwargs': {'normalize': False, 'cumulative': False, },
        'index': 0,
        'xlabel': 'Bin',
        'ylabel': 'Count',
    },
    'pmf': {
        # PMFs have discrete, exact values as bins rather than ranges (finite bin widths)
        #   but this histogram configuration doesn't distinguish between PMFs and PDFs,
        #   since mathematically they have all the same properties.
        #    PDFs just have a range associated with each discrete value
        #    (which should be when integrating a PDF but not when summing a PMF where the "width" is uniformly 1)
        'name': 'Probability Mass Function',   # probability density function, probability distribution [function]
        'kwargs': {'normalize': True, 'cumulative': False, },
        'index': 1,
        'xlabel': 'Bin',
        'ylabel': 'Probability',
    },
    'cmf': {
        'name': 'Cumulative Probability',
        'kwargs': {'normalize': True, 'cumulative': True, },
        'index': 2,
        'xlabel': 'Bin',
        'ylabel': 'Cumulative Probability',
    },
    'cfd': {
        'name': 'Cumulative Frequency Distribution',
        'kwargs': {'normalize': False, 'cumulative': True, },
        'index': 3,
        'xlabel': 'Bin',
        'ylabel': 'Cumulative Count',
    },
}


np = pd.np

tld_iana = pd.read_csv(os.path.join(DATA_PATH, 'tlds-from-iana.csv'), encoding='utf8')
tld_iana = OrderedDict(sorted(zip((tld.strip().lstrip('.') for tld in tld_iana.domain),
                                  [(sponsor.strip(), -1) for sponsor in tld_iana.sponsor]),
                              key=lambda x: len(x[0]),
                              reverse=True))
# top 20 in Google searches per day
# sorted by longest first so .com matches before .om (Oman)
tld_popular = OrderedDict(sorted([
    ('com', ('Commercial', 4860000000)),
    ('org', ('Noncommercial', 1950000000)),
    ('edu', ('US accredited postsecondary institutions', 1550000000)),
    ('gov', ('United States Government', 1060000000)),
    ('uk',  ('United Kingdom', 473000000)),  # noqa
    ('net', ('Network services', 206000000)),
    ('ca',  ('Canada', 165000000)),  # noqa
    ('de',  ('Germany', 145000000)),  # noqa
    ('jp',  ('Japan', 139000000)),  # noqa
    ('fr',  ('France', 96700000)),  # noqa
    ('au',  ('Australia', 91000000)),  # noqa
    ('us',  ('United States', 68300000)),  # noqa
    ('ru',  ('Russian Federation', 67900000)),  # noqa
    ('ch',  ('Switzerland', 62100000)),  # noqa
    ('it',  ('Italy', 55200000)),  # noqa
    ('nl',  ('Netherlands', 45700000)),  # noqa
    ('se',  ('Sweden', 39000000)),  # noqa
    ('no',  ('Norway', 32300000)),  # noqa
    ('es',  ('Spain', 31000000)),  # noqa
    ('mil', ('US Military', 28400000)),
    ], key=lambda x: len(x[0]), reverse=True))

uri_schemes_iana = sorted(pd.read_csv(os.path.join(DATA_PATH, 'uri-schemes.xhtml.csv'),
                                      index_col=0).index.values,
                          key=lambda x: len(str(x)), reverse=True)
uri_schemes_popular = ['chrome-extension', 'example', 'content', 'bitcoin',
                       'telnet', 'mailto',
                       'https', 'gtalk',
                       'http', 'smtp', 'feed',
                       'udp', 'ftp', 'ssh', 'git', 'apt', 'svn', 'cvs']

# these may not all be the sames isinstance types, depending on the env
FLOAT_TYPES = (float, np.float16, np.float32, np.float64, np.float128)
FLOAT_DTYPES = tuple(set(np.dtype(typ) for typ in FLOAT_TYPES))
INT_TYPES = (int, np.int0, np.int8, np.int16, np.int32, np.int64)
INT_DTYPES = tuple(set(np.dtype(typ) for typ in INT_TYPES))
NUMERIC_TYPES = tuple(set(list(FLOAT_TYPES) + list(INT_TYPES)))
NUMERIC_DTYPES = tuple(set(np.dtype(typ) for typ in NUMERIC_TYPES))

DATETIME_TYPES = (datetime.datetime, pd.datetime, np.datetime64)
DATE_TYPES = (datetime.datetime, datetime.date)

# matrices can be column or row vectors if they have a single col/row
VECTOR_TYPES = (list, tuple, np.matrix, np.ndarray)
MAPPING_TYPES = (Mapping, pd.Series, pd.DataFrame)

# These are the valid dates for all 3 datetime types in python (and the underelying integer nanoseconds)
INT_MAX = INT64_MAX = 2 ** 63 - 1
INT_MIN = INT64_MIN = - 2 ** 63
UINT_MAX = UINT64_MAX = - 2 ** 64 - 1

INT32_MAX = 2 ** 31 - 1
INT32_MIN = - 2 ** 31
UINT32_MAX = - 2 ** 32 - 1

INT16_MAX = 2 ** 15 - 1
INT16_MIN = - 2 ** 15
UINT16_MAX = - 2 ** 16 - 1

# Pandas timestamps can handle nanoseconds? by python datetimestampes cannot.
MAX_TIMESTAMP = pd.Timestamp('2262-04-11 23:47:16.854775', tz='utc')
MIN_TIMESTAMP = pd.Timestamp(pd.datetime(1677, 9, 22, 0, 12, 44), tz='utc')
ZERO_TIMESTAMP = pd.Timestamp('1970-01-01 00:00:00', tz='utc')

# to_pydatetime() rounds to microseconds, ignoring 807 nanoseconds available in other MAX TIMESTAMPs
MIN_DATETIME = MIN_TIMESTAMP.to_pydatetime()
MAX_DATETIME = MAX_TIMESTAMP.to_pydatetime()
MIN_DATETIME64 = MIN_TIMESTAMP.to_datetime64()
MAX_DATETIME64 = MAX_TIMESTAMP.to_datetime64()
INF = pd.np.inf
NAN = pd.np.nan
NAT = pd.NaT


# str constants
MAX_CHR = MAX_CHAR = chr(127)
APOSTROPHE_CHARS = "'`’"
UNPRINTABLE = ''.join(set(chr(i) for i in range(128)) - set(string.printable))
string.unprintable = UNPRINTABLE  # monkey patch so import string from this module if you want this!

NULL_VALUES = set(['0', 'None', 'null', "'"] + ['0.' + z for z in ['0' * i for i in range(10)]])
# if datetime's are 'repr'ed before being checked for null values sometime 1899-12-30 will come up
NULL_REPR_VALUES = set(['datetime.datetime(1899, 12, 30)'])
# to allow NULL checks to strip off hour/min/sec from string repr when checking for equality
MAX_NULL_REPR_LEN = max(len(s) for s in NULL_REPR_VALUES)

PERCENT_SYMBOLS = ('percent', 'pct', 'pcnt', 'pt', r'%')
FINANCIAL_WHITESPACE = ('Flat', 'flat', ' ', ',', '"', "'", '\t', '\n', '\r', '$')
FINANCIAL_MAPPING = (('k', '000'), ('M', '000000'))

# MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
# MONTH_PREFIXES = [m[:3] for m in MONTHS]
# MONTH_SUFFIXES = [m[3:] for m in MONTHS]
# SUFFIX_LETTERS = ''.join(set(''.join(MONTH_SUFFIXES)))
