

class Person:
    # osztályváltozók
    name = "John"
    age = 36
    country = "hu"

    def _protected(self):
        pass

    def __private(self):
        pass

    def public(self):
        pass


ertek = getattr(Person, 'age')
# print(ertek)

setattr(Person, 'age', 40)
ertek = getattr(Person, 'age')

# print(ertek)

# print(hasattr(Person, 'name'))


class Cica(object):
    def __init__(self, nev = "default_cica_nev_very_ok"):
        self._nev = nev                              # protected
        self.__privat = f"{self._nev} privát attr"   # privát

    def __str__(self):
        return f'cica: {self._nev}'

    def get_privat(self):
        return self.__privat

    def __eq__(self, other):
        if isinstance(other, Cica):
            return self._nev == other._nev
        return False

    @property
    def nev(self):
        print("getattr")
        return self._nev

    @nev.setter
    def nev(self, value):
        print("setter")
        if value == "cirmi":
            print("nem lehet ilyen név")
            return

        self._nev = value


c = Cica("cirmi")
c2 = Cica("cirmi2")
c_nevtelen = Cica()

print(f"cica :3 -> c:{c} --- c2:{c2} --- c_nevtelen:{c_nevtelen}")
print(f'cicaEgyezés: {c == c2}')
print(f'hibás cica: {c == 4}')
print(f"c név: {c._nev} - privát: {c.get_privat()}")

print("*" * 50)

print(c.nev)

c.nev = "cirmi_teszter"

print(c.nev)

c.nev = "cirmi"