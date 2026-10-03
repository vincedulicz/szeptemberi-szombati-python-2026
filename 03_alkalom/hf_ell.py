
def lista_letrehozasa(lista_hossza = 42):
    """ Param(s): lista_hossza: int 0 > """
    # TODO: check lista_hossza value...
    # count

    result = []
    i = 0

    # do_while -> for | végtelen ciklus -> kilpés ha a feltétel igaz

    while True:
        if len(result) == lista_hossza:
            break

    # for i in range(0, lista_hossza + 1):
        if i % 5 != 0:
            if i % 2 == 0:
                result.append(i * 3)
            else:
                result.append(i * 5 / 2)

        i += 1

    return result
    # [MI AZ AMIT EL AKAROK KÖVETNI for len(list) FELTÉTEL]

    # return [(i * 3 if i % 2 == 0 else i * 5 / 2) for i in range(0, lista_hossza) if i % 5 != 0]


# print(f"values: {lista_letrehozasa(62)} - len: {len(lista_letrehozasa(62))}")


""" 2. feladat """


TANULOK = [
    {"nev": "Teszt Elek", "osztaly": "13I", "eletkor": 19},
    {"nev": "Kiss Béla", "osztaly": "12A", "eletkor": 18},
    {"nev": "Nagy Anna", "osztaly": "11B", "eletkor": 17},
    {"nev": "Szabó Gergő", "osztaly": "10C", "eletkor": 16},
    {"nev": "Varga László", "osztaly": "9D", "eletkor": 15},
    {"nev": "Tóth Zsófia", "osztaly": "12A", "eletkor": 18}
]

OSZTALYOK = ["9A", "10B", "11C", "12D", "13I"]

import random

def get_tanulo_ertek_by_nev(nev):
    """ tanuló összes adat """
    return next(tanulo for tanulo in TANULOK if tanulo["nev"] == nev)

def kiir_tanulok():
    """ kiírja a tanulóakat formázottan """
    print("a jelenlegi tagok")

    # for
    for index, tanulo in enumerate(TANULOK, start=1):
        print(f'{index}. {tanulo["nev"]} {tanulo["eletkor"]} éves és a {tanulo["osztaly"]} osztályba jár.')

    # comp
    #   [print(f'{index}. {tanulo["nev"]} {tanulo["eletkor"]} éves és a {tanulo["osztaly"]} osztályba jár.') for index, tanulo in enumerate(TANULOK, start=1)]

def uj_tanulo():
    """ új tanuló hozzáadása a listához """
    nev = input("add meg az új tag nevét: ")
    eletkor = int(input("add meg az életkort: "))

    osztaly = random.choice(OSZTALYOK)

    TANULOK.append(
        {
            "nev": nev, 
            "osztaly": osztaly, 
            "eletkor": eletkor
        }
    )

    print(f'Új tag hozzáadva: {nev}, {eletkor} éves, {osztaly} osztály')

def tanulo_torlese():
    """ tanuló törlése a listából """
    nev = input("add meg a törlendő tag nevét: ")
    talalat = get_tanulo_ertek_by_nev(nev)
    print(talalat)

    if talalat:
        megerosites = input("Biztosan ki akarod törölni? (I/N): ")
        if megerosites.lower() == "i":
            TANULOK.remove(talalat)
            print(f'{nev} törölve lett a listából')
        else:
            print("törlés visszavonva")
    else:
        print("nem található ilyen nevű tag")

def tanulo_modositasa():
    nev = input("add meg a módosítani kívánt tag nevét: ")

    talalat = get_tanulo_ertek_by_nev(nev)
    if talalat:
        kulcs = input("melyik adatot szeretnéd módosítani? (nev, osztaly, eletkor): ")

        if kulcs in talalat:
            uj_ertek = input(f'add meg az új értéket a(z) {kulcs} mezőhöz')

            if kulcs == "eletkor":
                uj_ertek = int(uj_ertek)

            talalat[kulcs] = uj_ertek

            print(f'{nev} {kulcs} értéke módosítva lett: {uj_ertek}')
        else:
            print("érvénytelen kulcs")
    else:
        print("nem található ilyen nevű tag")



def main():
    while True:
        print(
            "Az alábbi parancsokat használhatod:"
            "\n1. Új tag - newmem | 2. Törlés - delete | 3. Módosítás - modify | Kilépés - end, Q, quit\n"
        )

        kiir_tanulok()

        parancs = input("mit szeretné' csinálni: ").strip().lower()
        if parancs in ["q", "end", "quit"]:
            print("a program leeáll")
            break
        elif parancs in ["newmem", "1"]:
            uj_tanulo()
        elif parancs in ["delete", "2"]:
            tanulo_torlese()
        elif parancs in ["modify", "3"]:
            tanulo_modositasa()
        else:
            print("érvénytelen parancs, próbálj újra...")

main()