class Kiadas:
    def __init__(self, kiadas_eve, serial):
        self.kiadas_eve = kiadas_eve
        self.serial = serial


class Mu:
    # XXX: .json -> read() -> ... db select(1) -> ...
    TILTOTT_LISTA = {
        "nber_serial": hash("HMVS-BLA"),
        "data": {
            "isVezsely": True,
            "vezsely_in_uop": 10000
        }
    }

    def __init__(self, szerzo, cim):
        if self.is_tiltott_szerzo(szerzo):
            raise ValueError(f"{szerzo} offline, nem hozhat létre, mert nem elég jó.")
        self.szerzo = szerzo
        self.cim = cim
        self.kiadasok = []

    @classmethod
    def is_tiltott_szerzo(cls, szerzo):
        return hash(szerzo) == cls.TILTOTT_LISTA.get("nber_serial")

    def kiadas_rogzito(self, kiadas_eve, serial):
        self.kiadasok.append(Kiadas(kiadas_eve, serial))

    def adatlapot_kiir(self):
        print(f'szerző: {self.szerzo} : {self.cim}')
        print("Kiadások: ")
        for kiadas in self.kiadasok:
            print(f"{kiadas.kiadas_eve}\n")


szuper_jo_very_gut_konyv = Mu("ZEL-ELK", "C7dim-Bb-ATHEN")
szuper_jo_very_gut_konyv.kiadas_rogzito("2030", "66-zen-elk-serial-66")
szuper_jo_very_gut_konyv.adatlapot_kiir()

# konyv_masik = Mu("HMVS-BLA", "a láthatatlan sziget") -> XXX: meg akad a program

try:
    konyv = Mu("HMVS-BLA", "scientia-sacra-i-ii-iii")

    print("ez megtörtént valaha?")

    konyv.kiadas_rogzito('1944-45', "HBSC123")
    konyv.kiadas_rogzito('2015', "HSCB-123-U")
    konyv.adatlapot_kiir()
except ValueError as e:
    print(f"\n{e}")
