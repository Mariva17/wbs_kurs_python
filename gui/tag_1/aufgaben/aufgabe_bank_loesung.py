"""
Problem: falls eine Abbuchung vorgenommen wird und die Überweisung fehlschlägt,
stimmen die Konten nicht mehr. 

Die Lösung wäre ein Rollback-Verfahren oder Datenbank-Tranksaktionen (SQL).
"""


class Konto:
    def __init__(self, initial: int, name: str) -> None:
        self.name = name
        self.balance = initial

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, value: int) -> None:
        if value < 0:
            raise ValueError("Der Kontostand darf nicht negativ sein!")
        self._balance = value

    def info(self):
        """Zeige den Kontostand an."""
        print(
            f"Der Kontostand von {self.name} beträgt {self.balance / 100}Euro"
        )

    def withdraw(self, amount: int) -> int:
        """Withdraw from account.

        Raises:
            TypeError if amount is not int
        """
        if not isinstance(amount, int):
            raise TypeError(
                "Es können nur ganzzahlige Werte übergeben werden."
            )

        self.balance = self.balance - amount

        return amount

    def deposit(self, amount: int) -> None:
        """Make deposit on account.

        Raises:
            TypeError if amount is not int
        """

        if not isinstance(amount, int):
            raise TypeError(
                "Es können nur ganzzahlige Werte übergeben werden."
            )

        self.balance = self.balance + amount


konto_1 = Konto(initial=10_000, name="Bob")
konto_2 = Konto(initial=1200, name="Alice")

value = konto_1.withdraw(amount=10_000)
konto_2.deposit(amount=value)
konto_1.info()
konto_2.info()
