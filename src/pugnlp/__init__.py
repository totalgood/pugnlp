# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'


# import os
# import importlib
# from pugnlp.futil import generate_files

# package_dir = os.path.dirname(__file__)

# file_infos = generate_files(package_dir, ext='.py')

# __all__ = []
# for info in file_infos:
#     if info['name'].startswith('__'):
#         continue
#     name = info['name'][:-3]
#     __all__ += [name]
#     globals()[name] = importlib.import_module('pugnlp.' + name)
