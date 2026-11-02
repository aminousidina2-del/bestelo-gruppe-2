class Produkt:
    def __init__(self, name: str, produktnummer: int, preis: float) -> None:
        self.name = name
        self.produktnummer = produktnummer
        self.preis = preis

    def __str__(self) -> str:
        return f"Produkt {self.produktnummer}: {self.name} ({self.preis} EUR)"

    def __repr__(self) -> str:
        return f"Produkt(name={self.name!r}, produktnummer={self.produktnummer}, preis={self.preis})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Produkt):
            return NotImplemented
        return self.produktnummer == other.produktnummer

    def __lt__(self, other: 'Produkt') -> bool:
        return self.preis < other.preis


class DigitalesProdukt(Produkt):
    def __init__(self, name: str, produktnummer: int, preis: float, dateigroesse_mb: float) -> None:
        super().__init__(name, produktnummer, preis)
        self.dateigroesse_mb = dateigroesse_mb

    def berechne_gesamtkosten(self) -> float:
        return self.preis


class PhysischesProdukt(Produkt):
    def __init__(self, name: str, produktnummer: int, preis: float, gewicht_kg: float) -> None:
        super().__init__(name, produktnummer, preis)
        self.gewicht_kg = gewicht_kg

    def berechne_gesamtkosten(self) -> float:
        return self.preis + (self.gewicht_kg * 2.5)

