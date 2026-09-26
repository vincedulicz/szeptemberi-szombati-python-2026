def szorzat(a, b): # függvény definiálása
    def_valtozo = 0

    if a == 1:
        def_valtozo = 99

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Mindkét paraméternek számnak kell lennie")
    return a * b

szam1 = input("szam1 ")
szam2 = input("szam2 ")

print(szorzat(int(szam1), szam2)) # függvény meghívása



def kisebb_duplaja(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Mindkét paraméternek számnak kell lennie")
    kisebb = a if a < b else b
    return kisebb * 2

# kisebb_duplaja(3, 4)

def is_paros_paratlan(szam):
    if not isinstance(szam, int):
        raise TypeError("Egész számot adj meg!")

    # is_method
    return szam % 2 == 0 # bool

    if szam % 2 == 0:
        print(f'ez a szám {szam} páros')
    else:
        print(f"ez a szám {szam} páratlan")

if is_paros_paratlan(5):
    print("páros / lesz")


def nagyobbTripla(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Mindkét paraméternek számnak kell lennie")
    nagyobb = a if a > b else b
    return nagyobb * 3


def szokoz_nelkul(szoveg):
    if not isinstance(szoveg, str):
        raise TypeError("A bemenetnek sztringnek kell lennie")
    return szoveg.replace(" ", "")