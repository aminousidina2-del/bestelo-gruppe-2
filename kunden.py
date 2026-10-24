class Kunde:
    def __init__(self, name: str, email: str):
        self._name = name
        self._email = email

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    def gib_rabatt(self, umsatz: float) -> float:
        return 0.0


class Privatkunde(Kunde):
    def __init__(self, name: str, email: str, geburtsjahr: int):
        super().__init__(name, email)
        self._geburtsjahr = geburtsjahr

    @property
    def geburtsjahr(self) -> int:
        return self._geburtsjahr

    def gib_rabatt(self, umsatz: float) -> float:
        if umsatz > 50: 
            return 0.5  
        return 0.0


class Geschäftskunde(Kunde):
    def __init__(self, name: str, email: str, ust_id: str):
        super().__init__(name, email)
        self._ust_id = ust_id

    @property
    def ust_id(self) -> str:
        return self._ust_id

    def gib_rabatt(self, umsatz: float) -> float:
        if umsatz > 1000:
            return 12  
        return 0.05


class Verein(Kunde):
    def __init__(self, name: str, email: str, vereinsregister: str):
        super().__init__(name, email)
        self._vereinsregister = vereinsregister

    @property
    def vereinsregister(self) -> str:
        return self._vereinsregister

    def gib_rabatt(self, umsatz: float) -> float:
        return 0.10
