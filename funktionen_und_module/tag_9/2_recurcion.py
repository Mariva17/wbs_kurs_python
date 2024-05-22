"""
Rekursion: Funktion ruft sich selbst auf, bis ein Basisfall eingetretten ist

"""

import math

print("factorial:", math.factorial(3)) # 3 * 2 * 1

def factorial(n):
    """rekursive Implementierung von Fakultät."""
    print("n:", n)

    if n < 0:
        raise ValueError("not defined for negative values")
    match n:
        case 1 | 0:
            return 1
        case _:
            return n * factorial(n-1)

    # if n == 1 or n == 0:
    #     return 1
    # else:
    #     result = n * factorial(n-1)
    #     return result
    

print("Fakultät:", factorial(3))

