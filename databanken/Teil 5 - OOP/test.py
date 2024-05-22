import sqlite3
import os


class Buch:

    def __init__(self, author, title):
        """Konstruktor der Klasse Buch
             Args:
                titel (str): Titel des Buches
                autor (str): Autor des Buches
        """
        self.author = author
        self.title = title

    def get_author(self):
        return self.author

    def get_title(self):
        return self.title


class Bibliothek:
    def __init__(self, datenbank):
        self.datenbank = datenbank

    def buch_hinzufuegen(self, buch):
        c = self.datenbank.verbindung.cursor()
        c.execute("INSERT INTO buecher (title, author) VALUES (?,?)", (buch.get_title, buch.get_author))
        self.datenbank.verbindung.commit()

    def anzeigen_buecher(self):
        c = self.datenbank.verbindung.cursor()
        result = c.execute("SELECT * FROM buecher").fetchall()
        for title, author in result:
            print(title, author)

    def suchen_buch(self, gesuchter_buch):
        c = self.datenbank.verbindung.cursor()
        result = c.execute("SELECT * FROM buecher WHERE title LIKE (?)", (gesuchter_buch,)).fetchall()
        for title, author in result:
            print(f"{title} von {author}")


class Datenbank:
    def __init__(self, pfad):
        self.verbindung = None
        self.pfad = pfad
        self.db_vorhanden = os.path.exists(pfad)
       # self.verbindung_herstellen()  # Es wird überprüft, ob eine Datenbank vorhanden ist.

    def verbindung_herstellen(self):
        if self.verbindung is None:
            self.verbindung = sqlite3.connect(self.pfad)

            if not self.db_vorhanden:
                self.datenbank_erstellen()

    def datenbank_erstellen(self):
        print("Datenbank wird erstellt")
        c = self.verbindung.cursor()
        sql = """CREATE TABLE IF NOT EXISTS buecher (
        title TEXT,
        author TEXT)        
        """
        c.execute(sql)


db = Datenbank('bibliothek.db')
db.verbindung_herstellen()  # Methode 'verbindung_herstellen()' wird aufgerufen, alternativ über Konstruktor
meine_bibliothek = Bibliothek(db)  # Bibliothek initialisieren

# Bücher hinzufügen
# meine_bibliothek.buch_hinzufuegen(Buch("George Orwell", "1984"))
# meine_bibliothek.buch_hinzufuegen(Buch("Aldous Huxley", "Brave New World"))
# meine_bibliothek.buch_hinzufuegen(Buch("Dostoyevskii", "Idiot"))
# meine_bibliothek.buch_hinzufuegen(Buch("O'Henry", "Cabbages and Kings"))

# Bücher anzeigen
# meine_bibliothek.anzeigen_buecher()
meine_bibliothek.suchen_buch("1984")




