pugnlp
======

Natural language processing utilities from the Portland Python user
group

Like pug-nlp(https://github.com/totalgood/pug-nlp), but simpler and
updated (python 2 and 3).

|Latest Version| |Latest Release| |Requirements Status| |Build Status|
|Documentation Status| |Coverage Status| |Code Climate| |Join the chat
at https://gitter.im/chatter\_bot/Lobby|

PUG Natural Language Processing (NLP) Utilities
-----------------------------------------------

This sub-package of the pug namespace package, provides natural language
processing (NLP) and text processing utilities built by and for the PDX
Python User Group (PUG).

--------------

Installation
------------

On a Posix System
~~~~~~~~~~~~~~~~~

You really want to contribute, right?

::

    git clone https://github.com/totalgood/pug-nlp.git

If you're a user and not a developer, and have an up-to-date posix OS
with the postgres, xml2, and xlst development packages installed, then
just use ``pip``.

::

    pip install pug-nlp

Fedora
~~~~~~

If you're on Fedora >= 16 but haven't done a lot of python binding
development, then you'll need some libraries before pip will succeed.

::

    sudo yum install -y python-devel libxml2-devel libxslt-devel gcc-gfortran python-scikit-learn postgresql postgresql-server postgresql-libs postgresql-devel
    pip install pug

Bleeding Edge
~~~~~~~~~~~~~

Even the releases are very unstable, but if you want to have the latest,
most broken code

::

    pip install git+git://github.com/hobsonlane/pug.git@master

Warning
~~~~~~~

This software is in alpha testing. Install at your own risk.

--------------

Development
-----------

I love merging PRs and adding contributors to the ``__authors__`` list:

::

    git clone https://github.com/totalgood/pug-nlp.git

.. |Latest Version| image:: https://img.shields.io/pypi/v/pugnlp.svg
   :target: https://pypi.python.org/pypi/pugnlp/
.. |Latest Release| image:: https://badge.fury.io/py/pugnlp.svg
   :target: https://pypi.python.org/pypi/pugnlp/
.. |Requirements Status| image:: https://requires.io/github/totalgood/pugnlp/requirements.svg?branch=master
   :target: https://requires.io/github/totalgood/pugnlp/requirements/?branch=master
.. |Build Status| image:: https://travis-ci.org/totalgood/pug-nlp.svg?branch=master
   :target: https://travis-ci.org/totalgood/pugnlp
.. |Documentation Status| image:: https://readthedocs.org/projects/chatterbot/badge/?version=stable
   :target: http://chatterbot.readthedocs.io/en/stable/?badge=stable
.. |Coverage Status| image:: https://img.shields.io/coveralls/totalgood/pugnlp.svg
   :target: https://coveralls.io/r/totalgood/pugnlp
.. |Code Climate| image:: https://codeclimate.com/github/totalgood/pugnlp/badges/gpa.svg
   :target: https://codeclimate.com/github/totalgood/pugnlp
.. |Join the chat at https://gitter.im/chatter\_bot/Lobby| image:: https://badges.gitter.im/chatter_bot/Lobby.svg
   :target: https://gitter.im/chatter_bot/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
