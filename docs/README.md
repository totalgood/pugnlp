# pugnlp

Natural language processing utilities from the Portland Python user group

Like pug-nlp(https://github.com/totalgood/pug-nlp), but simpler and updated (python 2 and 3).

[![Latest Version](https://img.shields.io/pypi/v/pugnlp.svg)](https://pypi.python.org/pypi/pugnlp/)
[![Latest Release](https://badge.fury.io/py/pugnlp.svg)](https://pypi.python.org/pypi/pugnlp/)
[![Requirements Status](https://requires.io/github/totalgood/pugnlp/requirements.svg?branch=master)](https://requires.io/github/totalgood/pugnlp/requirements/?branch=master)
[![Build Status](https://travis-ci.org/totalgood/pug-nlp.svg?branch=master "Travis Build & Test Status")](https://travis-ci.org/totalgood/pugnlp)
[![Documentation Status](https://readthedocs.org/projects/chatterbot/badge/?version=stable)](http://chatterbot.readthedocs.io/en/stable/?badge=stable)
[![Coverage Status](https://img.shields.io/coveralls/totalgood/pugnlp.svg)](https://coveralls.io/r/totalgood/pugnlp)
[![Code Climate](https://codeclimate.com/github/totalgood/pugnlp/badges/gpa.svg)](https://codeclimate.com/github/totalgood/pugnlp)
[![Join the chat at https://gitter.im/chatter_bot/Lobby](https://badges.gitter.im/chatter_bot/Lobby.svg)](https://gitter.im/chatter_bot/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


## PUG Natural Language Processing (NLP) Utilities

This sub-package of the pug namespace package, provides natural language processing (NLP) and text processing utilities built by and for the PDX Python User Group (PUG).

---

## Installation

### On a Posix System

You really want to contribute, right?

    git clone https://github.com/totalgood/pug-nlp.git

If you're a user and not a developer, and have an up-to-date posix OS with the postgres, xml2, and xlst development packages installed, then just use `pip`.

    pip install pug-nlp

### Fedora

If you're on Fedora >= 16 but haven't done a lot of python binding development, then you'll need some libraries before pip will succeed.

    sudo yum install -y python-devel libxml2-devel libxslt-devel gcc-gfortran python-scikit-learn postgresql postgresql-server postgresql-libs postgresql-devel
    pip install pug

### Bleeding Edge

Even the releases are very unstable, but if you want to have the latest, most broken code

    pip install git+git://github.com/hobsonlane/pug.git@master

### Warning

This software is in alpha testing.  Install at your own risk.

---

## Development

I love merging PRs and adding contributors to the `__authors__` list:

    git clone https://github.com/totalgood/pug-nlp.git


