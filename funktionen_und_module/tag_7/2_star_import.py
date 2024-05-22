"""
Star-Import: alles aus einem Modul importieren
from modulename import *

BAD PRACTICE!
"""
import random
from random import *
import numpy as np # Alias
import matplotlib.pyplot as plt
import random as randy

print(randint(3, 6))


def choices():
    print("...")

choices()

randy.gauss() # über den randy-Namespace Alias