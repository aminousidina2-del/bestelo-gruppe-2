from kunden import Privatkunde, Geschaeftskunde
from produkte import PhysischesProdukt
from bestellungen import Bestellung

def test_kunden():
    pk = Privatkunde("Anna", "anna@example.com", 1, 1995)
    assert pk.rabattsatz() == 0.0

    gk = Geschaeftskunde("Ben", "ben@example.com", 2, "Firma", "DE123")
    assert gk.rabattsatz() == 0.03

def test_bestellung():
    kunde = Geschaeftskunde("Ben", "ben@example.com", 2, "Firma", "DE123")
    produkt = PhysischesProdukt("Laptop", 10, 1000.0, 2.0)
    bestellung = Bestellung(100, kunde, [produkt])
    
    assert bestellung.gesamtpreis_berechnen() == 974.85

