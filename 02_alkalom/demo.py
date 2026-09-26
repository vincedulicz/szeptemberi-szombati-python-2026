
def string_muveletek():
    szoveg = "teszer elek kis és NAGY big az ok jó"

    print(len(szoveg)) # hossza

    print(f"0. index {szoveg[0]}") # iterálható objektum!!! indexelhető

    print(szoveg.replace("e", "é"))

    if "hamvas" not in szoveg:
        print("de jó nincs benne")
    else:
        print("hát van...")

    print(f"kezdő: {szoveg.startswith("teszter")} | végződik: {szoveg.endswith("jo")}")

    if szoveg.startswith("6"):
        print("számmal kezdődik")
    else:
        print("nem szám...")


def string_muvetelek__ii():
    szoveg = "Hello"

    lista = list(enumerate(szoveg))

    # a,b = foo() # -> tuple

    for index, value in enumerate(szoveg):
        print(f"{index}:{value}")

    print(lista)

    nevek = ["pista", "józsi", "béla"]
    elotag = "simple_basic_vezetknevet:"

    for utotag in nevek:
        print(elotag + utotag)

    print(elotag.find("basic"))

    szoveg.lower() # -> kisbetűs
    szoveg.upper() # -> nagybetűs
    szoveg.capitalize() # -> 0index nagy lesz
    szoveg.title() # -> Minden Egyes Karakter
    print("     whitespace lecsípés      ").strip()
    szoveg.lstrip() # bal oldali whitespace
    szoveg.rstrip() # jobb oldala -.-

    szoveg.count("A") # hány db A betű van

    szoveg.split(".") # szoveg.valami.123 -> ["szoveg", "valami", "123"]

    print("123".isdigit())
    print("hello".isalpha())
    print("hello123".isalnum())
    print("SponGbeBoB".swapcase()) # kicsi to nagy és nagy to kicsi

# string_muvetelek__ii()



def var_swapping():
    a = 5
    b = 4

    print(f"kezdő: a: {a} - b: {b}")

    tmp = a
    a = b
    b = tmp

    print(f"csere: a: {a} - b: {b}")

    a, b = b, a

    print(f"megint: a: {a} - b: {b}")

# var_swapping()



def primkereso():
    from math import sqrt

    szam = int(input("szám: "))

    if szam == 1:
        print("def szerint nem prím")
    else:
        is_prim = True

        n = 2
        while n <= sqrt(szam):
            if szam % n == 0:
                is_prim = False

            n += 1

        if is_prim:
            print("prím")
        else:
            print("nem prím")


# primkereso()


def szorzat(a, b, param = None):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("mindkét paraméternek számnak kell lennie")

    if param:
        print(f"p: {param}")
        return "yenayena"

    return a * b



def return_teszer(is_ok):
    pass


print(szorzat(3, 7))
print(szorzat(2, 2))

try:
    eredmeny = szorzat("2", 3)
except TypeError as e:
    print(f"e: {e}")


print("de jó")

