"""
(leicht)

Gegeben sind drei Listen:
cities 
continents 
population

Gebe jeweils die Städte in folgender Form aus 


Berlin (Europa): 3700000
Dehli (Asia): 19000000

"""

cities = ["Tokyo", "Delhi", "Shanghai", "Sao Paulo", "Mumbai", "Cairo", "Beijing", "Dhaka", "Mexico City", "Osaka"]
continents = ["Asia", "Asia", "Asia", "South America", "Asia", "Africa", "Asia", "Asia", "North America", "Asia"]
populations = [37393000, 31870000, 25779000, 22352000, 22186000, 20484965, 20035455, 21000000, 20996000, 19281000] 

for city, continent, population in zip(cities, continents, populations):
    print(f"{city}, ({continent}):, {population}")


