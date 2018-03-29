#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Constants and discovered values, like path to current installation of pug-nlp."""
from __future__ import division, print_function, absolute_import, unicode_literals
from builtins import (  # noqa
    bytes, dict, int, list, object, range, str,
    ascii, chr, hex, input, next, oct, open,
    pow, round, super,
    filter, map, zip)

import pandas as pd
from nltk.tokenize.casual import casual_tokenize


from gensim.corpora import Dictionary
from gensim.models import LsiModel, TfidfModel

try:
    from twote.models import Tweet
except ImportError:
    from openchat.models import Tweet
np = pd.np


if __name__ == '__main__':
    qs = Tweet.objects.filter(is_strict__gte=13)
    tweets = np.array(qs.values_list('pk', 'text', 'user__screen_name', 'user__is_bot'))
    tweets = pd.DataFrame(np.array(tweets), columns='pk text user is_bot'.split())
    tweets = tweets.set_index('pk', drop=True)
    tweets['tokens'] = tweets.text.apply(casual_tokenize)

    vocab = Dictionary(tweets.tokens)
    tfidf = TfidfModel(dictionary=vocab, id2word=vocab)
    bows = pd.Series(vocab.doc2bow(toks) for toks in tweets.tokens)
    lsi = LsiModel(tfidf[bows], num_topics=80, id2word=vocab, extra_samples=100, power_iters=2)
    lsi.save('/home/hobs/src/hackor/twote/data/lsi{}x{}x{}.saved'.format(len(tweets), lsi.num_topics, lsi.num_terms))
    topics = lsi[tfidf[bows]]
    topics = pd.DataFrame([dict(d) for d in topics], index=tweets.index, columns=range(80))
