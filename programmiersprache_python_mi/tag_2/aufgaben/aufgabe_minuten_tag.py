""" (MITTEL)
Rechne die angegebnen Minuten in Tage, Stunden und Minuten um
nutze dazu floordiv und modulo

MINUTES_DAY = 24 * 60 

Wieviele Tage sind 3434 Minuten?
Wieviele Stunden und Minuten bleiben dann noch übrig?

---------------------------------------------------------------
Beispiel

minuten = 3434 

sind 2 Tage, 9 Stunden und 14 Minuten

"""
total_mins = 3434
MINUTES_DAY = 24 * 60 
num_tage = total_mins // MINUTES_DAY
rest_minuten = total_mins % MINUTES_DAY
stunden = rest_minuten // 60
minuten = rest_minuten % 60
print(num_tage, "Tage,", stunden, "Stunden,", minuten, "Minuten")
