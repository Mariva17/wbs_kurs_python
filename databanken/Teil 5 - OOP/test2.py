
import sqlite3
import os

#  Christian Mielke

class Buch:

    def __init__(self, titel: str, autor: str) -> None:
        """Konstruktor der Klasse Buch

        Args:
            titel (str): Titel des Buches
            autor (str): Autor des Buches
        """
        self.titel = titel
        self.autor = autor

    def __del__(self) -> None:
        """Destruktor der Klasse Buch"""
        pass

    def get_titel(self) -> str:
        """Liefert den Titel des Buches zurück

        Returns:
            self.titel: Titel des Buches
        """
        return self.titel

    def get_autor(self) -> str:
        """Liefert den Autor des Buches zurück

        Returns:
            self.autor: Autor des Buches
        """
        return self.autor


class Bibliothek:
    def __init__(self, datenbank) -> None:
        """Konstrukter der Klasse Bibliothek

        Args:
            datenbank (Datenbank): Objekt der Klasse Datenbank
        """
        self.datenbank = datenbank

    def buch_hinzufuegen(self, buch) -> None:
        """Buch der Bibliothek hinzufuegen

        Args:
            buch (Buch): Liefert das einzufügende Buch-Objekt
        """
        c = self.datenbank.verbindung.cursor()
        c.execute("""INSERT INTO buecher (titel, autor) VALUES (?, ?)""", (buch.get_titel(), buch.get_autor()))
        self.datenbank.verbindung.commit()

    def buch_suchen(self, gesuchter_titel: str) -> None:
        """Buch aus List heraussuchen

        Args:
            gesuchter_titel (str): titel des gesuchten Buches

        Prints:
            Buchtitel und den Autor
        """
        c = self.datenbank.verbindung.cursor()
        result = c.execute("""SELECT titel, autor FROM buecher WHERE titel LIKE ?""", (gesuchter_titel, )).fetchall()
        print("Buchtitel, Autor")
        for titel, autor in result:
            print(f"{titel}, {autor}")

    def buecher_anzeigen(self) -> None:
        """Zeigt eine Liste aller Bücher der Bibliothek an"""
        c = self.datenbank.verbindung.cursor()
        result = c.execute("""SELECT titel, autor FROM buecher""").fetchall()
        print("Buchtitel, Autor")
        for titel, autor in result:
            print(f"{titel}, {autor}")

        print("*" * 50)

    def statistik_anzeigen(self) -> None:
        """Zeigt einige Zusatzinformationen wie die Maximalanzahl der Entitäten der DB an

        Prints:
            Maximalanzahl der Entitäten in der Tabelle
            Die zwei am häufigsten vorkommenden Autoren
            Die zwei am seltensten vorkommenden Autoren
        """
        print("Sonstige Informationen")
        print("-" * 50)

        c = self.datenbank.verbindung.cursor()
        result_count = c.execute("""SELECT COUNT(*) FROM buecher""")
        for count in result_count:
            print(f"Gesamtanzahl Einträge: {count[0]}")

        print("-" * 50)

        result_max = c.execute("""SELECT autor, COUNT(autor) FROM buecher 
                                  GROUP BY autor ORDER BY COUNT(autor) DESC LIMIT 2""")
        print("Häufgiste Autoren:", end=" ")
        for autor, anzahl in result_max:
            print(f"{autor} ({anzahl})", end=", ")

        print()
        print("-" * 50)

        result_min = c.execute("""SELECT autor, COUNT(autor) FROM buecher 
                                  GROUP BY autor ORDER BY COUNT(autor) ASC LIMIT 2""")
        print("Seltenste Autoren:", end=" ")
        for autor, anzahl in result_min:
            print(f"{autor} ({anzahl})", end=", ")

        print()
        print("-" * 50)


class Datenbank:

    def __init__(self, pfad: str) -> None:
        """Konstruktor der Klasse Datenbank

        Args:
            pfad (str): Der Pfad zur Datenbank
        """
        self.verbindung = None
        self.pfad = pfad
        self.db_vorhanden = os.path.exists(self.pfad)

    def verbindung_herstellen(self) -> None:
        """Erstellt eine neue Instanz einer Datenbankverbindung, sofern keine besteht"""
        if self.verbindung is None:
            self.verbindung = sqlite3.connect(self.pfad)

            if not self.db_vorhanden:
                self.datenbank_erstellen()

    def datenbank_erstellen(self) -> None:
        """Erstellt eine neue Tabelle buecher falls noch nicht vorhanden"""
        c = self.verbindung.cursor()
        sql = """CREATE TABLE IF NOT EXISTS buecher (
            titel TEXT,
            autor TEXT
        )"""
        c.execute(sql)


db = Datenbank("Bibliothek.db")
db.verbindung_herstellen()

meine_bibliothek = Bibliothek(db)
meine_bibliothek.buch_suchen("1984")
meine_bibliothek.buecher_anzeigen()
meine_bibliothek.statistik_anzeigen()
