
def list_comp():
    parosok = [value for value in range(1, 21) if value % 2 == 0]
    
    parosok_basic = []
    for value in range(1, 21):
        if value % 2 == 0:
            parosok_basic.append(value)

    print(f"parosok: {parosok} - parosok_basic: {parosok_basic}")


def list_comp():
    szavak = ["alma", "körte"]
    nagybetus = [szo.upper() for szo in szavak]

    print(nagybetus)

def dict_comp():
    basic_dict = {"x": 42}

    negyzet_dict = {x: x**2 for x in range(1, 6)}
    print(negyzet_dict)

    print(negyzet_dict.keys())
    print(negyzet_dict.values())
    print(negyzet_dict.items())



