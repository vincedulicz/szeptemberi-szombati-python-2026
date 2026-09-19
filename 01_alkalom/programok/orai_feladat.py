import random
import math


def elso_feladat():
    print("Hello, világ!")


def masodik_feladat():
    szam = int(input("Adj meg egy számot: "))
    print(szam)


def harmadik_feladat():
    szam1 = int(input("Adj meg egy számot: "))
    szam2 = int(input("Adj meg még egy számot: "))

    osszeg = szam1 + szam2

    print("Az összeg:", osszeg)


def negyedik_feladat():
    szam1 = int(input("Adj meg egy számot: "))
    szam2 = int(input("Adj meg még egy számot: "))

    print("Különbség:", szam1 - szam2)
    print("Szorzat:", szam1 * szam2)

    if szam2 != 0:
        print("Hányados:", szam1 / szam2)
    else:
        print("Nullával nem lehet osztani!")


def otodik_feladat():
    nev = input("Add meg a neved: ")

    print("Szia,", nev + "!")


def hatodik_feladat():
    szelesseg = float(input("Add meg a téglalap szélességét: "))
    magassag = float(input("Add meg a téglalap magasságát: "))

    terulet = szelesseg * magassag

    print("A téglalap területe:", terulet)


def hetedik_feladat():
    r = float(input("Add meg a kör sugarát: "))

    kerulet = 2 * math.pi * r
    terulet = math.pi * r * r

    print("A kör kerülete:", kerulet)
    print("A kör területe:", terulet)


def nyolcadik_feladat():
    szam = int(input("Adj meg egy számot: "))

    if szam % 2 == 0:
        print("A szám páros.")
    else:
        print("A szám páratlan.")


def kilencedik_feladat():
    for i in range(1, 11):
        print(i)


def tizedik_feladat():
    for i in range(2, 101, 2):
        print(i)


def tizenegyedik_feladat():
    osszeg = 0

    for i in range(1, 101):
        osszeg += i

    print("Az összeg:", osszeg)


def tizenkettedik_feladat():
    szo = input("Adj meg egy szót: ")

    darab = 0

    for i in szo:
        darab += 1

    print("A betűk száma:", darab)


def tizenharmadik_feladat():
    szoveg = input("Adj meg egy szöveget: ")

    darab = 0

    for i in szoveg:
        if i == "a":
            darab += 1

    print('Az "a" betűk száma:', darab)


def tizennegyedik_feladat():
    szam = int(input("Adj meg egy számot: "))

    for i in range(1, 11):
        print(szam, "*", i, "=", szam * i)


def tizenotodik_feladat():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def tizenhatodik_feladat():
    szo = input("Adj meg egy szót: ")

    print(szo[::-1])


def tizenhetedik_feladat():
    szo = input("Adj meg egy szót: ")

    visszafele = szo[::-1]

    if szo == visszafele:
        print("A megadott szó palindrom.")
    else:
        print("A megadott szó nem palindrom.")


def tizennyolcadik_feladat():
    szam1 = int(input("1. szám: "))
    szam2 = int(input("2. szám: "))
    szam3 = int(input("3. szám: "))
    szam4 = int(input("4. szám: "))
    szam5 = int(input("5. szám: "))

    legnagyobb = szam1

    if szam2 > legnagyobb:
        legnagyobb = szam2

    if szam3 > legnagyobb:
        legnagyobb = szam3

    if szam4 > legnagyobb:
        legnagyobb = szam4

    if szam5 > legnagyobb:
        legnagyobb = szam5

    print("A legnagyobb szám:", legnagyobb)
    
    
def tizennyolcadik_feladat_jobb():
    szamok = []

    for i in range(1, 6):
        szam = int(input(f"{i}. szám: "))
        szamok.append(szam)

    legnagyobb = max(szamok)

    print("A legnagyobb szám:", legnagyobb)


def tizenkilencedik_feladat():
    osszeg = 0

    while True:
        szam = int(input("Adj meg egy számot (0 = vége): "))

        if szam == 0:
            break

        osszeg += szam

    print("A számok összege:", osszeg)


def huszadik_feladat():
    gondolt_szam = random.randint(1, 100)

    print("Gondoltam egy számra 1 és 100 között.")

    while True:
        tipp = int(input("Tippelj: "))

        if tipp < gondolt_szam:
            print("Nagyobb számra gondoltam.")
        elif tipp > gondolt_szam:
            print("Kisebb számra gondoltam.")
        else:
            print("Eltaláltad!")
            break


# elso_feladat()
# masodik_feladat()
# harmadik_feladat()
# negyedik_feladat()
# otodik_feladat()
# hatodik_feladat()
# hetedik_feladat()
# nyolcadik_feladat()
# kilencedik_feladat()
# tizedik_feladat()
# tizenegyedik_feladat()
# tizenkettedik_feladat()
# tizenharmadik_feladat()
# tizennegyedik_feladat()
# tizenotodik_feladat()
# tizenhatodik_feladat()
# tizenhetedik_feladat()
# tizennyolcadik_feladat()
# tizenkilencedik_feladat()
# huszadik_feladat()