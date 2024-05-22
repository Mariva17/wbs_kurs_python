"""
1) Schreibe eine Funktion random_password,
die ein zufälliges Passwort erstellt.

Die Funktion soll mit Keyword-Argumenten
aufrufbar sein, die definieren, welche
Zeichen in dem Passwort enthalten sein müssen.

Das Passwort muss mindestens einen Großbuchstaben, mindestens einen
Kleinbuchstaben (beides aus ASCII), mindestens eine Zahl und mindestens ein Sonderzeichen
enthalten und 8 Zeichen lang sein.

Der Aufruf der random_password - Funktion
password = random_password(upper=1, lower=1, special=1, digits=1, length=8)

Nutze dazu die choice und  shuffle - Methode aus dem random-Modul,
sowie die passenden Variablen des string-Moduls (ascii_uppercase sowie
ascii_lowercase sowie digits).


2) Erstelle eine Funktion generate_passwords, die N (N=100_000) Passwörter
   erstellt und in Form einer Passwort - Liste zurückgibt.

password_list = generate_passwords(N)


3) Erstelle eine Funktion char_count_from_list(), die eine Liste mit Strings
entgegennimmt und die Vorkommen der einzelnen Zeichen zählt (total_char_count).
Zähle damit die Vorkommen in der Passwortliste. Welche 5 Zeichen wurden am häufigsten genutzt?

total_char_count = char_count_from_list(password_list)

Nutze dafür das Collections Modul und insbesondere die Counter-Klasse mit der
Methode most_common.
https://realpython.com/python-counter/


Alle Funktionen benötigen zumindest eine Summary (Single Line Docstring) sowie
vollständiges Type-Hinting der Parameter und Rückgabewerte.
"""
import string
import random
from collections import Counter

#random.seed(42)



def random_password(upper=1, lower=1, special=1, digits=1, length=8):
   
   s_b = random.choice(string.ascii_uppercase)
   s_s = random.choice(string.ascii_lowercase)
   num = random.choice(string.digits)
   symb = random.choice(string.punctuation)
   
   data = [s_b, s_s, num, symb]
   random.shuffle(data)
   #password = random.choices(data, k=8)
   #password = "".join(password)
   while not (upper and lower and special and digits and length):
      for i in data:
         
         password = random.choices(data, k=8)
         password = data.append(i)

         return password
   

print(random_password(upper=1, lower=1, special=1, digits=1, length=8))





