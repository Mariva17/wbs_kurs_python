"""
Erstelle eine Klasse Card, die eine Spielkarte repräsentiert.
Erstelle eine Klasse Deck, die ein Kartendeck repräsentiert.

Card:
Die Klasse Card hat zwei Attribute suit (Farbe) und rank (Wert).
Sie wird wie folgt Instanziiert

card = Card(suit=Suit.HEARTS, rank=Rank.10)

Deck:
Die Klasse Deck erstellt ein Kartendeck und mischt dieses (random.shuffle).
Sie bietet die Methode deal(number), die eine Anzahl an Karten ausgibt.
Ist number > als die Anzahl der Karten im Deck, wird ein ValueError ausgelöst.

Die vorhandenen Farben und Werte könnten als Enum angelegt werden.
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks =  [
        "TWO",
        "THREE",
        "FOUR",
        "FIVE",
        "SIX",
        "SEVEN",
        "EIGHT",
        "NINE",
        "TEN",
        "JACK",
        "QUEEN",
        "KING",
        "ACE",
    ],
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

Beispiel:

deck = Deck()
deck.shuffle()
cards = deck.deal(number=4)
print(cards)

Card('queen', 'diamonds')
Card('two', 'diamonds')
Card('six', 'hearts')
Card('six', 'clubs')

cards = deck.deal(number=124)
DeckExhaustedError! Nicht genug Karten im Deck!

Zusatzaufgabe: implementiere das Iterator-Prtokoll für die Klasse Deck.
nutze dazu zum Beispiel __iter__ und __next__

for card in deck:
    print(card)

"""
