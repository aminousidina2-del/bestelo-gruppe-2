class Bestellung:
    def __init__(self, bestellnummer: int, kunde, produkte: list) -> None:
        self.bestellnummer = bestellnummer
        self.kunde = kunde
        self.produkte = produkte

    def __str__(self) -> str:
        return f"Bestellung Nr: {self.bestellnummer} für Kunde: {self.kunde.name}"

    def __repr__(self) -> str:
        return f"Bestellung(bestellnummer={self.bestellnummer}, kunde={self.kunde!r}, produkte={self.produkte!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Bestellung):
            return NotImplemented
        return self.bestellnummer == other.bestellnummer

    def gesamtpreis_berechnen(self) -> float:
        summe = 0.0
        for produkt in self.produkte:
            if hasattr(produkt, "berechne_gesamtkosten"):
                summe += produkt.berechne_gesamtkosten()
            else:
                summe += produkt.preis
        
        rabatt_satz = self.kunde.rabattsatz()
        endpreis = summe * (1 - rabatt_satz)
        
        if endpreis < 0:
            return 0.0
        return round(endpreis, 2)
