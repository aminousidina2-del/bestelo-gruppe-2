class Kunde:
    def __init__(self, name: str, email: str, kundennummer: int) -> None:
        self.name = name
        self.email = email
        self.kundennummer = kundennummer

    def begruessung(self) -> str:
        return f"Hallo {self.name}!"

    def rabattsatz(self) -> float:
        return 0.0


class Privatkunde(Kunde):
    def __init__(self, name: str, email: str, kundennummer: int, geburtsjahr: int) -> None:
        super().__init__(name, email, kundennummer)
        self.geburtsjahr = geburtsjahr


class Geschaeftskunde(Kunde):
    def __init__(self, name: str, email: str, kundennummer: int, firmenname: str, ust_id: str) -> None:
        super().__init__(name, email, kundennummer)
        self.firmenname = firmenname
        self.ust_id = ust_id

    def begruessung(self) -> str:
        return f"Sehr geehrte Damen und Herren der {self.firmenname},"

    def rabattsatz(self) -> float:
        return super().rabattsatz() + 0.03


class Verein(Kunde):
    def __init__(self, name: str, email: str, kundennummer: int, vereinsregisternummer: str) -> None:
        super().__init__(name, email, kundennummer)
        self.vereinsregisternummer = vereinsregisternummer

    def begruessung(self) -> str:
        return f"An den Vorstand des Vereins {self.name}"

    def rabattsatz(self) -> float:
        return 0.05

