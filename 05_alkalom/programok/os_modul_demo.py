import os, shutil
import math, time

def dir_test():
    try:
        if not os.path.exists("example_nem_letezik.txt"):
            with open("example_nem_letezik.txt", "w") as f:
                f.write("hello world")
    except FileNotFoundError as e:
        print(e)

    print(f"munka könyvtár: {os.getcwd()}")


# dir_test()

def os_muveletek():
    os.mkdir("teszt_mappa")
    print(os.listdir("."))


    # txt_files = []
    # for f in os.listdir("."):
    #     if f.endswith(".txt"):
    #         txt_files.append(f)

    txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]

    print(f"txt files: {txt_files}")

    print(f"méret: {os.path.getsize("example.txt")}")

    if os.name == "nt":
        os.system("dir")
    else:
        os.system("ls")


    base_path = os.getcwd()
    file_path = os.path.join(base_path, "folder", "file.txt")

    print(f"full path: {file_path} - type: {type(file_path)}")


def tmp_file():
    with open("tempfile.tmp", "w") as temp_file:
        temp_file.write("tmp data...")

    print("created tmp")

    time.sleep(5)

    os.remove("tempfile.tmp")

    print("törölve várakozással")


def env_var():
    os.environ["NEW_ENV_VAR"] = "pyprogramscript"
    print(f"new_env_var: {os.getenv("NEW_ENV_VAR")}")

    for key, value in os.environ.items():
        print(f"k: {key} | v: {value}")

# env_var()


def foo():
    print("foo eleje")
    time.sleep(3)
    print("foo vége")


# start_time = time.time()
# foo()
# end_time = time.time()
# print(f"runtime: {end_time - start_time} sec")



class Nber:
    OSZTALYVALTOZO = 0

    def __init__(self, nev = "default_name"):
        print("init object...")
        self.nev = nev

    def __str__(self):
        return f"az object_nber neve: {self.nev}"

    def nev_kiir(self):
        print(f"neve: {self.nev}")


def nber_object_vizsg():
    nber1 = Nber()
    print(f'nber1 object: \n type: {type(nber1)} \n nber1 neve: {nber1.nev}\n')

    nber2 = Nber("Teszt Elek")
    print(f'nber2 object: \n type: {type(nber2)} \n nber2 neve: {nber2.nev}')

    print(f"\nnber1 class_var: {nber1.OSZTALYVALTOZO} \n nber2 class_var: {nber2.OSZTALYVALTOZO} \n Nber class_var: {Nber.OSZTALYVALTOZO}")


nber_jozsi = Nber("Józsi")
print(type(nber_jozsi))

nber_jozsi.nev_kiir()

nber_pista = Nber("Pista")
nber_pista.nev_kiir()

print(f"\nnber_pista {nber_pista}")