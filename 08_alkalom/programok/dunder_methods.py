
class Number:
    # TODO: Segedfüggvényt felvenni a duner metódusok/függvényekhez,
    #       hogy az other object tényleg Number típusú objektum-e.
    #       isinstance(other, Number) -> elkövetés | Err
    def __init__(self, value):
        self._value = value

    @staticmethod
    def is_other_self_object(other):
        # TODO: implement
        return other

    @property
    def value(self):
        print("getter")
        return self._value

    @value.setter
    def value(self, new_value):
        print("setter")
        if new_value != 0:
            self._value = new_value
        print("nem lehet 0!")

    def __eq__(self, other):
        """ obj1 == obj2 """
        # self.is_other_self_object(other) # XXX: fixme
        return self.value == other.value

    def __ne__(self, other):
        """ obj1 != obj2 """
        return self.value != other.value

    def __add__(self, other):
        """ obj1 + obj2 """
        return Number(self.value + other.value)

    def __iadd__(self, other):
        """ obj1 += obj2 """
        print("iadd")
        if other.value == 10:
            print("10-et nem lehet hozzáadni")
            return
        self.value += other.value
        return self

    def __lt__(self, other):
        """ obj1 < obj2 """
        return self.value < other.value

    def __gt__(self, other):
        """ obj1 > obj2 """
        return self.value > other.value

    def __le__(self, other):
        """ obj1 <= obj2 """
        return self.value <= other.value

    def __ge__(self, other):
        """ obj1 >= obj2"""
        return self.value >= other.value

    def __str__(self):
        """ string repr """
        return f'number object: {self.value}'

    def __repr__(self):
        """ dev repr """
        return f'Number({self.value})'


# str(Number(1)) -> __str__ f"{Number(3)}" -> user
# repr(Number(2)) -> __repr__ -> developer
# 
# 
# n = Number(1)
# n2 = Number(2)
# 
# uj = n + n2
# 
# n += n2

szam = Number(32)
masik_szam = Number(39)

print(f"szam: {szam}")

print(szam < masik_szam)

szam += masik_szam
print(f"iadd után a szam: {szam}")

# TODO: többi dunder meghívása