"""(Mittel)
Schreiben Sie ein Python-Skript, das:

Eine variable email definiert, die eine E-Mail-Adresse in Form
von benutzername@domain.tld enthält.

Sie sollten diese Adresse so wählen, dass sie sowohl einen Benutzernamen
als auch eine Domain mit einer Top-Level-Domain (TLD) beinhaltet, zb. .com

Den Benutzernamen und die Domain der E-Mail-Adresse separat identifiziert
und in zwei verschiedenen Variablen speichert, indem Sie die
find-Methode für Strings verwenden.

Die identifizierten Teile der E-Mail-Adresse (Benutzername und Domain)
sowie die TLD der Domain ausgibt. Die TLD ist der Teil nach dem letzten Punkt
in der E-Mail-Adresse.

Anforderungen:

- Verwenden Sie die find-Methode, um die Position des "@"-Zeichens und des letzten Punktes (".") in der E-Mail-Adresse zu finden.
-Sie dürfen keine Schleifen oder selbst definierten Funktionen verwenden.
- Die Ausgabe soll klar den Benutzernamen, die Domain ohne TLD und die TLD selbst darstellen.

Plausiblitätsprüfung:
- Falls das @ Zeichen fehlt oder kein Punkt in der Domain vorhanden ist, soll eine Fehlermeldung ausgegeben werden.
- auf weitere Fehler muss nicht geprüft werden.

Beispiele:
------------

Bitte geben Sie eine Email-Addresse ein: max.mustermann@example.com.

Benutzername: max.mustermann
Domain: example
TLD: com


Bitte geben Sie eine Email-Addresse ein: max.mustermann
Fehlerhafte Eingabe. Bitte geben Sie eine gültige Email-Adresse ein.


Bitte geben Sie eine Email-Addresse ein: max.mustermann@example
Fehlerhafte Eingabe. Bitte geben Sie eine gültige Email-Adresse ein.

Hinweise:
---------
nutze find, rfind und slicing
"""
user_input = input("Bitte geben Sie eine Email-Addresse ein:")

el1 = user_input.find("@")

if el1 > 0:
    el2 = user_input.rfind(".")

    if  el2 > el1:
        name = user_input[:el1]
        domain = user_input[el1+1:el2]
        tld = user_input[el2+1:]
        print(f"Benutzname: {name} \n Domain: {domain} \n TLD: {tld}")
    
    else:
        print("Fehlerhafte Eingabe.")
    
else:   
    print(
        "Die E-Mail-Adresse ist ungültig. "
        "Sie muss ein '@' und nach diesem ein '.' enthalten."
        "Das @-Symbol darf nicht am Anfang stehen"
    )
    

