"""(Schwer)
**Aufgabe: Analyse von Netzwerkdaten**

Du arbeitest als Netzwerkadministrator in einem Unternehmen und bist für die Überwachung und Analyse des Netzwerkverkehrs verantwortlich. 
Du hast eine Liste von Netzwerkdatenpaketen erhalten, die Informationen über die Übertragung von Daten zwischen verschiedenen Computern im Netzwerk enthalten.

Die Liste `netzwerkdaten` enthält Listen, wobei jede Liste die folgenden Informationen über ein Datenpaket enthält: Absender-IP-Adresse, Ziel-IP-Adresse, 
Paketgröße in Kilobyte und Protokoll (z. B. TCP, UDP).


netzwerkdaten = [
    ["192.168.1.10", "192.168.1.20", 2.5, "TCP"],
    ["192.168.1.15", "192.168.1.30", 1.8, "UDP"],
    ["192.168.1.20", "192.168.1.10", 3.2, "TCP"],
    ["192.168.1.30", "192.168.1.25", 2.0, "UDP"],
    ["192.168.1.10", "192.168.1.25", 4.5, "TCP"],
    ["192.168.1.25", "192.168.1.20", 1.3, "UDP"],
    ["192.168.1.20", "192.168.1.15", 2.7, "TCP"],
    ["192.168.1.25", "192.168.1.10", 3.8, "UDP"],
    ["192.168.1.30", "192.168.1.20", 2.1, "TCP"],
    ["192.168.1.10", "192.168.1.30", 2.9, "UDP"]
]


Deine Aufgabe ist es, folgende Statistiken und Analysen durchzuführen:

1. Berechne die Gesamtanzahl der Datenpakete in der Liste.
2. Ermittle die durchschnittliche Paketgröße.
3. Finde heraus, wie viele Datenpakete TCP und wie viele UDP verwenden.
4. Bestimme die IP-Adressen, die die meisten Datenpakete als Absender und als Ziel haben.
5. Erstelle eine Liste `grosse_pakete`, die nur die Datenpakete enthält, deren Größe größer als 2 Kilobyte ist.
6. Bestimme, ob es irgendwelche Datenpakete gibt, die von einem Computer an sich selbst gesendet wurden (Absender-IP-Adresse ist gleich der Ziel-IP-Adresse).

"""
netzwerkdaten = [
    ["192.168.1.10", "192.168.1.20", 2.5, "TCP"],
    ["192.168.1.15", "192.168.1.30", 1.8, "UDP"],
    ["192.168.1.20", "192.168.1.10", 3.2, "TCP"],
    ["192.168.1.30", "192.168.1.25", 2.0, "UDP"],
    ["192.168.1.10", "192.168.1.25", 4.5, "TCP"],
    ["192.168.1.25", "192.168.1.20", 1.3, "UDP"],
    ["192.168.1.20", "192.168.1.15", 2.7, "TCP"],
    ["192.168.1.25", "192.168.1.10", 3.8, "UDP"],
    ["192.168.1.30", "192.168.1.20", 2.1, "TCP"],
    ["192.168.1.10", "192.168.1.30", 2.9, "UDP"]
]
