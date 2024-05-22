"""
Modul - Docstring

"""

def wool_amount(sheep, wool):
    """Menge Wolle, die ein Shaf im Monat im Schnitt produziert."""


def wool_amount_google(sheep, wool):
    """Menge Wolle, die ein Shaf im Monat im Schnitt produziert.
    
    Die Menge an Wolle, die eine Schafherde im Monat
    und co weiter.

    Args:
        sheep: die Anzahl die Schafe
        wool: die durchschnittliche Wollmenge

    Returns:
        int: durchschnittliche Wollmenge im Monat
    """
    return sheep * wool


def wool_amount_numpy(sheep, wool):
    """Menge Wolle, die ein Shaf im Monat im Schnitt produziert.
    
    Die Menge an Wolle, die eine Schafherde im Monat
    und co weiter.

    Auslesen mit Sphinx:
    
    Parameters:
    --------------------
    sheep : int
        die Anzahl die Schafe
    wool : int
        die durchschnittliche Wollmenge

    Returns:
    -------------------
    int 
        durchschnittliche Wollmenge im Monat


    See also
    --------------------
    Average : Weighted average
    
    """




wool_amount(23, 100)
print(wool_amount_google.__doc__)