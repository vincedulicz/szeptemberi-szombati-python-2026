print("Hello world!")

import keyword

print(keyword.kwlist)


full_name = "Dulicz" \
            "Vince"

kereszt_nev = "Vince"

s = """ Valmilyen
szöveg
szöveg1
szöveg2
full_name
 """


teszt = 0

print(full_name, kereszt_nev, s, teszt)

print(f"Full name: {full_name} - kereszt_nev: {kereszt_nev} - \n {s}")



szam = 1
print(type(szam))


szoveg = "arra vall"
szoveg_extension = ", hogy minden gyönyört megismerjen "
szoveg_newer = "és belefulladjon"

full_szoveg = szoveg + szoveg_extension + szoveg_newer
print(f'\nFull szöveg value: {full_szoveg} - ugyanaz: {szoveg + szoveg_extension + szoveg_newer}')

print(f"\nszoveg alap típus {type(szoveg)} - value: {szoveg}")
szoveg = 1234
print(f"\nszoveg new value: {szoveg} - típus: {type(szoveg)}")


# isinstance(a_int, int): True / False

a_int = 1
b_float = 1.5
c_complex = 3.14j

print(f"\n{type(c_complex)}")

print("\n*************\n")

print(5 / 2)    # osztás -> float
print(5 // 2)   # egészosztás -> int
print(7 % 2)    # maradékosztás
print(2 ** 3)   # hatványozás
print(2 * 3)    # szorzás

print("\n*************\n")

lista = [
    "string", 1, None, ["..."]
]

print(f"lista hosszú: {len(lista)}")

print(f"\n lista 0-ás indexű elem ami a lista 1. értéke {lista[0]}")
print(f"\n lista 1-es indexű elem ami a lista 2. értéke {lista[1]}")
print(f"\n lista 2-es indexű elem ami a lista 3. értéke {lista[2]}")
print(f"\n lista 3-es indexű elem ami a lista 4. értéke {lista[3]}")
# print(f"\n lista 4-es indexű elem ami a lista 5. értéke {lista[4]}") # -> indexerror-t dob

print("\n*************\n")

szoveg = "Karakterek hiphopperek látjátok a világ kerek"

print(f"szoveg hossza: {len(szoveg)}")
print(szoveg[0])        # első karakter
print(szoveg[0:2])      # első két karakter
print(szoveg[2:])       # utolsóig megy a 3. karaktertől
print(szoveg[-3:])      # utolsó 3 karekter

print(szoveg[-1])       # utolsó karekter

print(szoveg[0:-1:2])   # elejétől az utolsó előttig, kettes lépésköz

print(szoveg[::2])      # elejétől a végégig kettes lépésközzel

print(szoveg[::1])      # teljes string

print(szoveg[::-1])     # visszafelé

print(szoveg[-2])       # utolsó előtti karakter


lista = [1, 2, 3, 4, 5, 6]
print(type(lista))

i = 0
while i <= len(lista) - 1:
    print(f"i értéke: {i}")
    print(f"érték: {lista[i]}, típus: {type(lista[i])}")
    i += 1 # i = i + 1
    print(f"i értéke: {i}")

print(len(lista))


print("\n*************\n")


# name = input()
# print(f"szia {name}")


print("\n*************\n")

# str(2) + str(2) = 22 default input az string!

# first_num = int(input("első szám: "))
# second_num = int(input("második szám: "))
# 
# print(f'összege: {first_num + second_num}') 


print("\n*************\n")


# print("mennyi a kör sugara: ")
# sugar = float(input())
# 
# 
# import math
# 
# print(f"pí: {math.pi}")
# print("kerulet = ", 2 * sugar * math.pi)
# print("terulet = ", sugar ** 2 * math.pi)


print("\n*************\n")

def paros_e_method_old(szam):
    if szam % 2 == 0:
        print("páros")
    else:
        print("páratlan")



szam = 2
print(szam % 2 == 0)



# def paros_e_method(szam: int) -> bool:
#     return szam % 2 == 0
# 
# szam = int(input("Szám bekérés: "))
# 
# if paros_e_method(szam): # True is Ture False is True
#     print("páratlan")
# else:
#     print("páros")
# 
# 
# if not False:
#     print("true ...")
# else:
#     print("false")
# 
# 
# if True:
#     print("az igaz")
# else:
#     print("nem érjük el sosem így...")


# szam = int(input("Szám bekérés: "))


print("\n*************\n")


a = 0
b = False   # 0
c = True    # 1

if a > b:
    print("a > b")
elif b > a:
    print("b nagyobb")
elif b == a:
    print("b = a")
else:
    print("más...")



print("\n*************\n")
print("\n*************\n")


def kiir(szam = 5):
    print(f"Kiir szám: {szam}")


kiir()  # default param szam = 5
kiir(2)
kiir(3)
kiir(4)
kiir(6)


print("\n*************\n")



lista = ["str", 2,2,2,2,2,3,4,5,6, 2j, 3.14, "str2", [":)"]]

print(lista)


lista.append(5)


print(lista)


print(lista.count("str")) # előfordulás megszámolása





def palindrom():
    szoveg = "Indul a görög aludni."

    csakbetuk = ""
    for i in szoveg:
        if i.isalnum():
            csakbetuk += i.lower()

    print(csakbetuk)

    hibas = False
    index = 0
    hossz = len(csakbetuk)
    while index < hossz / 2:
        if csakbetuk[index] != csakbetuk[hossz - 1 - index]:
            hibas = True
            break
        index += 1

    if hibas:
        print("nem palindrom")
    else:
        print("palindrom")

# palindrom()


def tizennyolcadik_fealadat(hanyszor):
    szamok = []

    for i in range(1, hanyszor):
        szam = int(input(f"{i}. szám: "))
        szamok.append(szam)

    legnagyobb = max(szamok)

    print(f"A legnagyobb szám: {legnagyobb}")


# tizennyolcadik_fealadat(6)


def tizenkilencedik_feladat():
    osszeg = 0

    while True:
        szam = int(input("Adj meg egy számot ( 0 = vége): "))

        if szam == 0:
            break

        osszeg += szam # osszeg = osszeg + szam

    print(f"A számok összege: {osszeg}")


# tizenkilencedik_feladat()



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


# tizenotodik_feladat()

