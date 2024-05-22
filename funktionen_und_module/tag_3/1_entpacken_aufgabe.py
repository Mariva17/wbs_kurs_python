
"""
Aufgabe:
für jeden Film soll die Funktion print_movie aufgerufen werden.
Wie muss die funktion aufgerufen werden?
Wie muss die Funktion implementiert sein?

Ergebnis:
The Matrix - Wachowski - 1999
The Terminator - James Cameron - 1984 - Gale Anne Hurd
"""


def print_movie(sep=" - ", **kwargs):
    """The Matrix - Wachowski - 1999"""
    print(*kwargs.values(), sep=sep)
    



movies = [
    {
        "title": "The Matrix",
        "director": "Wachowski",
        "year": 1999,
    },
    {
        "title": "The Terminator",
        "director": "James Cameron",
        "year": 1984,
        "producer": "Gale Anne Hurd",
    },
]

for movie in movies:
    print_movie(**movie)
