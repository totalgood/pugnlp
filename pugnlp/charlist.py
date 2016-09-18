r"""
Character Sets (strings, sequences, lists) printable and nonprintable ASCII characters

Similar to the constants in strings module (which are included here for convenience too),
like `strings.printable`, `strings.letters`, `strings.lowercase`, etc

>>> digits
'0123456789'
>>> '1' in ascii_all
True
>>> '1' in nondigit
False
>>> '+' in nondigit
True
>>> all_ascii  # notice that the `all()` builtin has NOT been overridden
'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a
\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f'
"""
from __future__ import division, print_function, absolute_import, unicode_literals
# from builtins import str
import string

printable = string.printable
uppercase = ascii_uppercase = string.ascii_uppercase
lowercase = ascii_lowercase = string.ascii_lowercase
letters = ascii_letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
whitespace = string.whitespace

printable_uppercase = digits + uppercase + '!"#$%&\'()*+,-./:;<= >?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
ascii_all = ('\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17' +
             '\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<= >' +
             '?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f')
ascii_nonlowercase = ('\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15' +
                      '\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<= >' +
                      '?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`{|}~\x7f')
# ascii_uppercase = ascii_nonlowercase
ascii_nonletter = ('\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !' +
                   '"#$%&\'()*+,-./0123456789:;<= >?@[\\]^_`{|}~\x7f')
# letters and digits removed from ascii_all
ascii_nonalphanum = ('\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !' +
                     '"#$%&\'()*+,-./:;<= >?@[\\]^_`{|}~\x7f')
# letters, digits and underscore removed from ascii_all
ascii_nonword = ('\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !' +
                 '"#$%&\'()*+,-./:;<= >?@[\\]^`{|}~\x7f')

# FIXME: duplicates "+" and seems wrong (don't other punctuation symbols need escaping?)
# PUNCTUATION_RE_CLASS = r'[-\+' + string.punctuation.replace('-', '') + r']'
not_digits = letters + punctuation + whitespace
not_digits_nor_sign = not_digits.replace('-', '').replace('+', '')
not_digits_nor_decimal = not_digits.replace('.', '')
not_digits_nor_sign_but_with_decimal = not_digits_nor_sign.replace('.', '')
not_letters = digits + punctuation + whitespace

unprintable = nonprintable = notprintable = ('\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17' +
                                             '\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x7f')
ascii_nondigit = ('\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14' +
                  '\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./:;<=>?@' +
                  'ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f')
