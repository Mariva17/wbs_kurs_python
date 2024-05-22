import sqlite3
import os


class Kunden:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Datenbank:
    def __init__(self, pfad):
        self.verbindung = None
        self.pfad = pfad
        self.db_vorhanden = os.path.exists(pfad)

    def verbindung_herstellen(self):
        if self.verbindung is None:
            self.verbindung = sqlite3.connect(self.pfad)

            if not self.db_vorhanden:
                self.datenbank_erstellen()

    def datenbank_erstellen(self):
        print("Datenbank wird erstellt")
        c = self.verbindung.cursor()
        sql = """CREATE TABLE IF NOT EXISTS kunden_verwaltung (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kunden_name TEXT,
        email TEXT)        
        """
        c.execute(sql)
        self.verbindung.commit()


class KundenVerwaltung:
    def __init__(self, datenbank):
        self.datenbank = datenbank

    def kunde_hinzufuegen(self, kunde):
        c = self.datenbank.verbindung.cursor()
        c.execute("INSERT INTO kunden_verwaltung(kunden_name, email) VALUES (?, ?)", (kunde.name, kunde.email))
        self.datenbank.verbindung.commit()

    def kunden_anzeigen(self):
        c = self.datenbank.verbindung.cursor()
        result = c.execute("SELECT * FROM kunden_verwaltung").fetchall()
        for id, name, email in result:
            print(id, name, email)

    def suchen_kunde(self, kunde):
        c = self.datenbank.verbindung.cursor()
        result = c.execute("SELECT * FROM kunden_verwaltung WHERE kunden_name LIKE (?)", (kunde,)).fetchone()
        print(result)


db = Datenbank('kunden.db')
db.verbindung_herstellen()

verwaltung = KundenVerwaltung(db)
# Kunden hinzufuegen
# verwaltung.kunde_hinzufuegen(Kunden("Max Mustermann", "max.must@gmail.com"))
# verwaltung.kunde_hinzufuegen(Kunden("Tom Lee", "tom-lee@gmail.com"))
# verwaltung.kunde_hinzufuegen(Kunden("Anna Norton", "anna.nt@test.com"))
# verwaltung.kunde_hinzufuegen(Kunden("Hanna Müller", "hanna_m@gmail.com"))

# verwaltung.kunden_anzeigen()
verwaltung.suchen_kunde("Tom%")

def menu():
    commands = ["Kunde hinzufuegen", "Kunden anzeigen", "Kunde suchen"]
    print("Welcome to Kunden verwaltung")


