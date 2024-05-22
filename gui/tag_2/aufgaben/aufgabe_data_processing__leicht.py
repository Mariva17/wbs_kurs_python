"""(leicht)
In diesem Beispiel gibt es zwei Klassen: DataProcessor und DatabaseHandler. Die
@staticmethod-Dekoratoren markieren die Methoden als statische Methoden, die
unabhängig von einer Instanz der Klasse aufgerufen werden können. DataProcessor
wird zum Laden und Manipulieren der Daten verwendet, während DatabaseHandler
zum Speichern der Daten in MongoDB dient.

Das Programm muss mit CSV-Dateien MIT und OHNE Header arbeiten können.

csv_data = CSVProcessor.load_csv("data.csv", header=["id", "alfa", "beta"])
db = MongoDBHandler(db="meine_datenbank")
db.save_csv(data=csv_data, collection="movies")
db.close()
"""
