
""" (MITTEL)
Bei der Körpergröße handelt es sich um ein annähernd
normalverteiltes Merkmal. Das bedeutet: Misst man die
Körpergröße einer größeren Zahl erwachsener deut-
scher Männer, so beträgt der Mittelwert ca. 178 cm. Um
diesen Mittelwert herum verteilen sich die meisten
Messwerte. Häufig findet sich die Angabe, wieviel Pro-
zent der Messwerte innerhalb einer bestimmten Stan-
dardabweichung liegen. Die Standardabweichung gibt
dabei an, wie stark die Messwerte von dem Mittelwert
abweichen und berechnet sich anhand feststehender
mathematischer Formeln.

Frauen:
Mittelwert: 166
Sigma: 9

Männer:
Mittelwert: 177,8
Sigma: 6.1

Aufgabe: Erstelle zwei Listen von 10000 zufälligen männlichen sowie weiblichen Körpergrößen.
Schreibe dazu die nötigen Funktionen und plotte die Histogramme.

"""

import random
import matplotlib.pyplot as plt

random.seed(42)

M = 10000
mu_m = 177.8
sigma_m = 6.1

values_men = [random.gauss(mu=mu_m, sigma=sigma_m) for _ in range(M)]
print("Männer:", values_men[:10])


W = 10000
mu_w = 166
sigma_w = 9

values_women = [random.gauss(mu=mu_w, sigma=sigma_w) for _ in range(W)]
print("Frauen:", values_women[:10])

plt.hist([values_men, values_women], bins=20, color=["blue", "green"])
plt.legend(["Männer", "Frauen"])
plt.grid()
plt.title("Körpergrößen: Männer und Frauen")
plt.show()