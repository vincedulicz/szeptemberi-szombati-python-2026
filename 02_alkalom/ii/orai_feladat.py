
def elso_feladat():
    db = [0] * 10

    print("számok 1-10 között, üres sor = vége: ")

    sor = input()

    while sor != "":
        try:
            szam = int(sor)
        except TypeError:
            print("type error tényleg")
            sor = input()
            continue
        finally:
            print("mindig lefut")

        # TODO: eldöntés 1-10 között van-e a szám
        #       ha nem megyünk tovább continue
        #       ha igen akkor elmentjük
        try:
            db[szam - 1] += 1
        except IndexError:
            print("exception ág")
            sor = input()
            continue

        sor = input()

    szam = 1
    while szam <= 10:
        print(f"{szam}: {db[szam - 1]} db")
        szam += 1


# elso_feladat()

def masodik_feladat():
    ev = int(input("év: "))

    def is_szokoev(ev):
        # XXX: általában az is_... függvények 1 sorosak
        if ev % 400 == 0:
            return True

        if ev % 4 == 0 and ev % 100 != 0:
            return True

        return False

    def is_szokoev_better(ev):
        return ev % 400 == 0 or (ev % 4 == 0 and ev % 100 != 0) # -> T or F |||| T or T ||| F or F

    print(is_szokoev(ev))
    print(is_szokoev_better(ev))


masodik_feladat()