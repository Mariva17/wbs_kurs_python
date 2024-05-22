"""
errno
https://docs.python.org/3/library/errno.html
Fehlermeldung für OS-level Operationen
"""

import errno

try:
    3 / 0
    f = open("gibtsnicht.txt")
except OSError as e:
    print(e.errno == errno.ENOENT)
except ArithmeticError as e:
    print(e.errno)
