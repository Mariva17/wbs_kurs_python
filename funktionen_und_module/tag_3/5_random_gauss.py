"""
Zufallswert aus einner Normalverteilung (Gauss)

mu 0= Muttelwert
sigma= Standard-Abweichung

"""


import random
import matplotlib.pyplot as plt

random.seed(42)

print(random.gauss(mu=0, sigma=1)) # Wert aus Std-Normal
print(random.gauss(mu=175, sigma=5))

# Alternative: normalvariate
print (random.normalvariate(mu=175, sigma=5))


N = 1000
mu = 340
sigma = 12

values = [random.gauss(mu=mu, sigma=sigma) for _ in range(N)]
print(values[:10])
plt.hist(values, bins=20)
plt.legend([f"{mu=}, {sigma=}"])
plt.grid()
plt.title("Normalverteilung")
plt.show()




