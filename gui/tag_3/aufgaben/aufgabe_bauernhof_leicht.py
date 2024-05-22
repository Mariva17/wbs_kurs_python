"""
Aufgabe: Einführung in die Vererbung mit einer Tierklasse

Aufgabenstellung:
Implementiere eine Klasse 'Animal', die ein Attribut 'name' enthält
und eine Methode 'sound', die einen allgemeinen Laut ausgibt.

Erstelle eine Unterklasse 'Dog', die von 'Animal' erbt. Überschreibe
die Methode 'sound', um einen spezifischen Laut ('Bark') auszugeben.
Nutze dabei die Funktion 'super()', um zunächst den Laut der
Oberklasse 'Animal' auszugeben und füge dann den spezifischen Laut
hinzu.

Beispiel:
- Eine Instanz von 'Animal' könnte "Animal makes a noise" ausgeben.
- Eine Instanz von 'Dog' könnte "Animal makes a noise, Dog says Bark" ausgeben.

Animal makes a noise
Animal makes a noise, Dog says Bark


"""

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} makes a noise"

    

class Dog(Animal):
    
    def sound(self):
        return super().sound() + ", Dog says Bark"
          


x = Animal(name="Bobby")
print(x.sound())

dog = Dog(name="Bonni")
print(dog.sound())


