"""

"""
import sys
import random

from random import randint#, choice
from copy import deepcopy
from pprint import pprint



def choice():
    print("my choice")

# Zugriff auf Funktion choice üder den namespace random
random.choice([1, 2])

randint(1, 4)

choice() # bezieht sich auf choice() aus Zeile 13 und nicht choice aus random


# Diese Module sind aktuell geladen:
print("*" * 40)
for key, value in sys.modules.items():
    print(key, value)