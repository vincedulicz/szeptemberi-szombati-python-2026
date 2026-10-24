import json
import os

def json_kezdet():
    adat = {
        # XXX: ékezet mentes kulcsok az ajánlott!!!
        "név": "Anna",
        "kor": 25,
        "város": "Bp"
    }

    json_string = json.dumps(adat)
    print(f"type: {type(json_string)} - adat: {json_string}")


    adat = json.loads(json_string)
    print(f"type: {type(adat)} - adat: {adat}")

    print(adat.get("névvvv", "NoData"))

    try:
        print(f"név: {adat["névvv"]}")
    except KeyError as e:
        print(f"hiba: {e}")


    # írás
    with open('adat.json', 'w', encoding='utf-8') as file:
        json.dump(adat, file, indent=4, ensure_ascii=False)


    # olvasás
    with open("adat.json", 'r', encoding='utf-8') as file:
        adat = json.load(file)
        print(type(adat))
        print(f"kor: {adat.get("kor")}")


def json_kozep():
    sample_json = """{
        "company":{
            "employee":{
                "name":"emma",
                "payble":{
                    "salary":7000,
                    "bonus":800
                }
            }
        }
    }"""

    data = json.loads(sample_json)
    print(type(data))

    print(data["company"]["employee"]["payble"]["salary"])

    try:
        print(data.get("company").get("employee"))
    except AttributeError as e:
        print("nincs cég")



def safe_json_read(filename: str) -> {}:
    # TODO: filename isObject(str) ??? bool -> 1/0
    # XXX: isinstance(object, (list, tuple))

    # debug:
    print(f"filename: {filename} - type{type(filename)}")

    if not isinstance(filename, (str)):
        return {"err": "nem str típusu a filename"}

    data = None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # return json.load(f)
            data = json.load(f)
            print(f"Sikeres beolvasás {filename}")
            return data
    except FileNotFoundError as e:
        print(f"Ez a fájl <{filename}> nem található...")
        data = {"err": f"e: {e}"}
    except json.JSONDecodeError as e:
        print("nem json formátumu objektum")
        data = {"err": f"e: {e}"}
    except Exception as e:
        print(f"más hiba van: {e}")
        data = {"err": f"e: {e}"}

    return data


# print(safe_json_read("hibas_adat.json"))
# print(safe_json_read(36.9)) # hiba


def save_json_write(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"sikeresen mentve {filename}")
    except (IOError, TypeError) as e:
        print(f"hiba történt: {e}")




def json_check_or_create(path, default_data=None):
    if not os.path.exists(path):
        print(f"nem létezik")
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(default_data or {}, f, indent=4, ensure_ascii=False)
    else:
        print(f'{path} már létezik')


def get_date():
    return "mai dátum import date.... 2026.10.24"

json_check_or_create(
    path="user_settings.json", 
    default_data={
        "settings": "verysetting", 
        "flag_": True, 
        "session_id": "8ghg498dfdf93483g984g39849g34",
        "timestamp": get_date(),
        "user": {
            "settings_": {
                "valami__": {
                    "na ezeket akkor eléred": [
                        "domain.name", 
                        "google.com", 
                        "127.0.0.1"
                    ]
                }
            }
        }
    }
)



def update_json_file(filename, new_data):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data.update(new_data)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f'{filename} frissítve')


# update_json_file("user_settings.json", {"other_settings_json_very_fontos_key": 369})



import shutil
from datetime import datetime


def backup_json(filename):
    if os.path.exists(filename):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{filename}.{ts}.bak"
        shutil.copy(filename, backup_name)
        print(f'backup elkészült: {backup_name}')



backup_json("user_settings.json")




