"""
Aufgabe (MITTEL), nutze map und filter
1. Rechne Temperaturliste von Celsius in Fahrenheit um
2. Filtere Einträge > THRESHOLD_FAHRENHEIT
3. Gebe den tiefsten Wert in Grad Fahrenheit sowie Grad Celsius an
"""

THRESHOLD_FAHRENHEIT = 77

# Beispiel Sensordaten (Temperaturwerte in Celsius)
sensor_data_celsius = [22, 24, 26, 28, 32, 35, 40, 18, 15, 42, 27, 30]

def fahrenheit(cel):
    return (cel * 9 / 5) + 32
sensor_data_celsius = list(map(fahrenheit, sensor_data_celsius))
result = min(filter(lambda x: x > 77, sensor_data_celsius))

print("Min fahrenheit: ", result)