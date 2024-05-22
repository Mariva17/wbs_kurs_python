"""(schwer)
Gegeben sind Listen mit Herzfrequenzwerten unterschiedlicher Länge.

freq_list_1 = [72, 88, 95, 102, 68, 120, 45, 80, 100, 110]
freq_list_2 = [85, 75, 60, 90, 120, 130, 55, 92, 65, 105]


Plausibilitätsprüfung der Daten: Überprüfe, ob die Werte in jeder Liste innerhalb des normalen Herzfrequenzbereichs von 40 bis 180 Schlägen pro Minute liegen. 
Unplausible Werte sollen rausgefiltert (d.h. entfernt) werden.

a) Berechne den Durchschnitt der plausiblen Herzfrequenzwerte für jede Liste.
b) Gestalte das Programm so, das unkompliziert weitere Listen hinzufgefügt werden könnte (freq_list_3, freq_list_4, ...).
Unkompliziert bedeutet, dass nicht das ganze Programm geändert werden muss, sondern nur an einer Stelle definiert und einer
anderen Liste hinzugefügt werden muss (Skalierbarkeit)


Beispiel:
------------
Der Durchschnittswert der plausiblen Werte für Liste 1 ist 88.0
Der Durchschnittswert der plausiblen Werte für Liste 2 ist 87.7


"""
freq_list_1 = [72, 88, 959, 102, 68, 120, 45, 80, 1900, 110, 20]
freq_list_2 = [85, 75, 960, 90, 120, 190, 55, 92, 65, 105]



