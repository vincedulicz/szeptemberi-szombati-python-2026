def foo():
    print("ok foo lefutott")

    return True


def maganhangzo_szamlalo():
    szoveg = input("adjá meg egy szöveget: ")
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"

    db = 0

    for betu in szoveg:
        if betu in maganhangzok:
            db += 1
        else: # érthetőség végett
            db += 0

    print(str(db) + " kk" + " ff")
    print(f"szöveg .... darabszám: {db} foo: {foo()}")

# maganhangzo_szamlalo()


def maganhangzo_szamlalo_rovidebb():
    szoveg = input("adjá meg egy szöveget: ")
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"

    print(f"Ennyi meg ennyi karakter és így: {sum(betu in maganhangzok for betu in szoveg)} db van benne ...") # -> sum( 1, 0, 0, 1 ) -> 1 + 0 + 0 + 1 = 2


# maganhangzo_szamlalo_rovidebb()



def szavak_visszafele():
    mondat = input("adjá meg egy mondatot: ")

    szavak = mondat.split("")

    print(f"szavak: {szavak} - type: {type(szavak)}")

    szavak.reverse()

    print(" ".join(szavak))

    jelszo = ""

    # if len(jelszo) >= 8 and any(karakter.islower() for karakter in jelszo) and any(...isupper()) and any(...isdigit()):
    #     pass

# szavak_visszafele()


def leggyakoribb_szam():
    from collections import Counter

    szamok = []

    while (adat := input().strip()):
        szamok.append(int(adat))

    if not szamok:
        print("nem adott meg számot...")
        return

    counter = Counter(szamok)

    counter.most_common(1) # list [(1, value)]
    legtobb_szam, legtobb_db = counter.most_common(1)[0]

    print(f"a legnagyobb elem: <{legtobb_szam}> és <{legtobb_db}> alkalommal fordult elő")

leggyakoribb_szam()