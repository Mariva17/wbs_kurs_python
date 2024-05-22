"""(Leicht)
Erstelle eine Klasse Konto mit den Methoden 
withdraw (Abbuchen)
deposit (Einzahlen)
info (Liefert Kontostand)

Erstelle zwei Konto-Instanzen und überweise Geld von einem Konto auf das
andere. Ein Konto darf nicht überzogen werden (< 0 Euro). Einheiten werden im
Finanzbereich in Cent-Beträgen angegeben.

Beispiel:
konto_1 = Konto(initial=10_000, name="Bob")
konto_2 = Konto(initial=1200, name="Alice")
konto_2.info()
Auf dem Konto befinden sich zur Zeit 12.00 Euro

# Validierung der Eingabe
konto_1.withdraw(amount="abc")
Dieser Vorgang ist nicht möglich!

# Überweisung von Konto 1 auf Konto 2
value = konto_1.withdraw(amount=100)
konto_2.deposit(amount=value)

Zusatz-Überlegungen
Was ist bei diesem Vorgehen problematisch? 

"""

class Konto:
    
    def __init__(self, initial, name_kontohaber) -> None:
        self.initial = initial
        self.name_kontohaber = name_kontohaber
        
    
    def deposit(self, amount):
        try:
            float(amount)
            self.initial += amount
            return print("Auf dem Konto befinden sich zur Zeit (nach Einzahlen) {:.2f} Euro.".format(self.initial / 100))
        except:
            print("Dieser Vorgang ist nicht möglich!")
        


    def withdraw(self, amount):

        if self.initial > 0:
            try:
                float(amount)
                self.initial -= amount
                print("Nach Abbuchen: ", self.initial)
                return amount * 100
            except:
                print("Dieser Vorgang ist nicht möglich!")
        else:
            print("Abbuchen ist nicht möglich.")

    

    def info(self):
        print("Auf dem Konto befinden sich zur Zeit {:.2f} Euro.".format(self.initial/100)) 

if __name__ == "__main__":
    konto_1 = Konto(initial=10_000, name_kontohaber="Bob")
    konto_2 = Konto(initial=1200, name_kontohaber="Alice")
    konto_2.info()
    konto_1.info()

    print("*" * 40)
    # Validierung der Eingabe
    konto_1.withdraw(amount="abc")

    # Überweisung von Konto 1 auf Konto 2
    value = konto_1.withdraw(amount=100)
    
    konto_2.deposit(amount=value)    