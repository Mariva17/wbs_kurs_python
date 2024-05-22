"""
Funktionsparameter und Argumente
Keyword - Argumente: kwargs

"""


def load_csv(file_name, encoding):
    print(f"{file_name=}, {encoding=}")


load_csv("test.csv", "utf-8") # Argumente per Position
load_csv(encoding="utf-8", file_name="test.csv") # Argumente per Keyword



def unbestimmte_kwargs(x, y, **kwargs):
    print(kwargs) # dict


unbestimmte_kwargs(x=3, y=4, name="Bob", age=24)


def connect_to_db(*, username, password, database):
    # alles rechts vom * MUSS als Keyword - Argument übergeben werden
    print(username, password, database)

connect_to_db(username= "Bob", password="abc123", database="main")
# Fehler! 
# connect_to_db("Bob", "abc123", "main")