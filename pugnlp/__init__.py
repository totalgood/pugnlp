import pkg_resources

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
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
