def olvasas():
    forrasfajl = open("autok_listaja.txt")

    for sor in forrasfajl:
        print(sor)

        print(forrasfajl.readline())

        print(forrasfajl.readlines())

        print(forrasfajl.read())

    forrasfajl.close()


def autok_adatgyujtes():
    autok = []
    with open('autok_listaja.txt', 'r', encoding='utf-8') as forrasfajl:
        for sor in forrasfajl:
            adatok = sor.strip().split(',')
            auto = {'rendszam': adatok[0], "típus": adatok[1], 'kor': int(adatok[2])} # TODO: check_value before storing
            autok.append(auto)

    print(f'autok: {autok}')


# autok_adatgyujtes()


def kiiras():
    with open('kiirando.txt', 'w', encoding='utf-8') as celfajl:
        print("ez kerül be ide a file-ba de amúgy printelek :)", file=celfajl)

# kiiras()


def kiiras_trukkos_ez_igy():
    with open("basic_kiir.txt", 'w', encoding='utf-8') as celfajl:
        celfajl.write('ide meg ez fog kerülni a txt-be')
        celfajl.writelines(['123\n', "\nszöveg\n", '\nlorem ipsum\n'])

# kiiras_trukkos_ez_igy()


def json_beolvas():
    import json

    with open('diakok.json', 'r', encoding='utf-8') as diakok_adatok:
        print(f'diakok_adatok type: {type(diakok_adatok)}')

        adatok = json.load(diakok_adatok)

        print(f'adatok type: {type(adatok)}')

        print(f"adatok: {adatok.get("diakok2", 'N/A')}\n")

        for diak in adatok['diakok']:
            print(f'diak név: {diak.get("név")}')

            if diak.get('kollegista'):
                print("mér nem")
            else:
                print("de")


json_beolvas()


def del_param():
    "ezzel majd user-t törlök"

    pass

def modify():
    """ ezzel fogok tudni modósítani use-reket .... """
    pass


def menu():
    valasztott = input("adjá meg valamit...: ")
    if valasztott == ["1", 'del']:
        del_param()
    elif valasztott == ["2", "mdf"]:
        modify()