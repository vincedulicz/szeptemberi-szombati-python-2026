

class LAMPA:
    piros = 1
    sarga = 2
    sargazold = 3
    zold = 4

auto = None

print(LAMPA.piros == auto)


class Menu:
    kilepes = 0
    stat = 1
    kiiras = 2
    beolvas = 3


quit = ["q, end, quit"]
user_input = input() # 1.2.3.4
if Menu.kilepes == user_input:
    sys.exit(1)
elif quit.__contains__(user_input):
    pass