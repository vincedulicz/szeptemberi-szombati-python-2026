
class Auto:
    gyartok = ["Toyota", "BMW", "Tesla"]

    def __init__(self, marka, modell, evjarat): # konstruktor -> példányosítjuk meg az osztály
        self.marka = marka      # publikus példányváltozó 
        self.modell = modell    # publikus példányváltozó
        self.evjarat = evjarat  # publikus példányváltozó
        self.__km_ora = 0       # privát példányváltozó

    def info(self):
        """ publikus függvény """
        return f'{self.evjarat} - {self.marka} - {self.modell} - {self.__km_ora}'

    def __titkos_ugras(self):
        """ privát metódus """
        print(f"{self.__km_ora} gyorsan ugrik előre")

    def _novenyesitett_ora(self):
        """ protected """
        self.__titkos_ugras()
        self.__km_ora += 10

    def uj_km(self, km):
        """ hol a hiba """
        if km > self.__km_ora:
            self.__km_ora = km
        else:
            print("Nem állíthatod vissza")

    @classmethod
    def gyartok_listaja(cls):
        return cls.gyartok

    @staticmethod
    def uzemanyag_koltseg(km, liter_ar):
        return km * 0.06 * liter_ar


auto = Auto("Toyota", "corolla", 2020)

print(Auto.gyartok) # osztályszintű osztályváltozó elérése

print(auto.gyartok)

print(auto.info())

auto.uj_km(15000)

auto._novenyesitett_ora()

print(auto.info())

print(f"elérhető gyártok: {Auto.gyartok_listaja()}")

print("üzemanyag költség: ", Auto.uzemanyag_koltseg(1000, 400), "Ft")