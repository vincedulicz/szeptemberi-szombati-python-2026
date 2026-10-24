def i_feladat():
    print("I. feladat")
    db = fej = ketfej = sorozat = 0
    for sor in open("kiserlet.txt"):
        d = sor.strip()
        if d == "":
            continue
        db += 1
        if d == "F":
            fej += 1
            sorozat += 1
        else:
            if sorozat == 2:
                ketfej += 1
            sorozat = 0
    if sorozat == 2:
        ketfej += 1

    print("1. feladat")
    print(f"A dobasok szama: {db}")
    print("2. feladat")
    print(f"A fejek aranya: {fej / db * 100:.2f}%")
    print("3. feladat")
    print(f"Pontosan ket egymas utani fej elofordulasainak szama: {ketfej}")


def ii_feladat():
    print("\nII. feladat")
    sakkozok = []
    for sor in open("sakk.txt", encoding="utf-8"):
        if sor[76:79] == "HUN":
            sakkozok.append([sor[15:76].strip(), sor[80], int(sor[113:117]), int(sor[126:130])])
    print("1. feladat")
    print(f"A beolvasott magyar sakkozók száma: {len(sakkozok)}")

    ferfiak = [s for s in sakkozok if s[1] == "M"]
    nok = [s for s in sakkozok if s[1] == "F"]
    print("2. feladat")
    print(f"A listában {len(ferfiak)} és {len(nok)} női sakkozónk szerepel")

    print("3. feladat")
    for lista, nem in ((ferfiak, "férfi"), (nok, "női")):
        legjobb = max(lista, key=lambda s: s[2])
        print(f"A legmagasabb pontszámú {nem} versenyzőnk {legjobb[0]}")
        print(f"Pontszáma: {legjobb[2]}")
        print(f"Születési éve: {legjobb[3]}")

    print("4. feladat")
    fiatal = [s for s in nok if s[3] >= 1990 and s[2] >= 2000]
    print(f"{len(fiatal)} olyan női sakkozónk van, aki 1990-ben vagy az után született, "
          f"és Élő-pontszáma legalább 2000")

    print("5. feladat")
    print("A Polgár család tagjai")
    csalad = [s for s in sakkozok if s[0].startswith("Polgar,")]
    for s in sorted(csalad, key=lambda s: s[2]):
        print(f"{s[0].split(', ')[1]:<9}{s[3]:<6}{s[2]}")

    print("6. feladat")
    judit = [s[2] for s in sakkozok if s[0] == "Polgar, Judit"][0]
    nevek = []
    for s in sakkozok:
        if s[2] >= judit and s[0] != "Polgar, Judit":
            csillag = "(*)" if s[2] >= 2735 else ""
            nevek.append(s[0].replace(",", "") + csillag)
    print("Akik elérték Polgár Judit 2021. februári pontszámát:")
    print(", ".join(nevek) + ".")


def iii_feladat():
    print("\nIII. feladat")
    for a in range(2, 17):
        for b in range(2, 17):
            try:
                x = int("110a10101", a)
                y = int("223313020003", b)
            except ValueError:
                continue
            if a != b and x == y:
                print(f"a) {x}")
                print(f"b) {a}")
                print(f"c) {b}")


def iv_feladat():
    print("\nIV. feladat")
    naplo = [sor.split() for sor in open("webstat.txt") if sor.strip() != ""]
    print("1. feladat")
    print(f"A beolvasott sorok száma: {len(naplo)}")

    print("2. feladat")
    napok = {}
    for s in naplo:
        napok[s[1]] = napok.get(s[1], 0) + 1
    for nap in napok:
        print(f"{nap}\t{napok[nap]} látogató")

    print("3. feladat")
    bongeszok = []
    for s in naplo:
        if s[0] != "-" and s[0] not in bongeszok:
            bongeszok.append(s[0])
    print("A böngészők: " + ", ".join(bongeszok))

    print("4. feladat")
    chrome = [s for s in naplo if s[0] == "Chrome"]
    forrasok = {}
    for s in chrome:
        forrasok[s[3]] = forrasok.get(s[3], 0) + 1
    for f in forrasok:
        print(f"{f}\t{forrasok[f] / len(chrome) * 100:.1f}%")

    print("5. feladat")
    napi = {}
    for s in naplo:
        napi[(s[1], s[2])] = napi.get((s[1], s[2]), 0) + 1
    tobbszor = []
    for nap, ip in napi:
        if napi[(nap, ip)] > 1 and ip not in tobbszor:
            tobbszor.append(ip)
    print("Amely címekről többször is jártak az oldalon egy adott napon: " + ", ".join(tobbszor))

    print("6. feladat")
    ip = input("Kérek egy IP címet: ")
    fajl = ip.replace(".", "_") + ".txt"
    with open(fajl, "w") as ki:
        for s in naplo:
            if s[2].split(".")[:2] == ip.split(".")[:2]:
                ki.write(f"{s[1]} {s[2]}\n")
    print(f"A {fajl} fájl elkészült.")


def main():
    i_feladat()
    ii_feladat()
    iii_feladat()
    iv_feladat()


main()