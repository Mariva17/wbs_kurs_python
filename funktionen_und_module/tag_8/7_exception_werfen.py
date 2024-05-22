"""

Eine Exception erheben (raise)

was tun, wenn eine Funktion kein Ergrbnis liefern kann?

"""
import math

#int("ighd")
#"test".index("x") # Value Error
print("test".find("x")) # liefert -1


def ellipse_area(grosse_halbachse: float, kleine_halbachse: float) -> float:
    """Berechnung der Ellipsenfläche
    
    Args:
        grosse_halbachse
        kleine_halbachse
    Reises:
        ValueError wenn kleine_halbachse > grosse_halbachse

    """
    if kleine_halbachse > grosse_halbachse:
        raise ValueError("b darf nicht größer als a sein")
    
    return kleine_halbachse * grosse_halbachse * math.pi

try:
    print("Fläche:", ellipse_area(8, 9))
except ValueError as e:
    print("Die Fläche konnte nicht errechnet werden.")
