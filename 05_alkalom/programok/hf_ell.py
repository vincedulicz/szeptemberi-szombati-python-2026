from datetime import date, datetime, timedelta
import math
import random
from statistics import mean, stdev

def get_today_info():
    today = date.today()

    return {
        "date": today,
        "weekday": today.strftime('%A'),
        "day_of_year": today.timetuple().tm_yday
    }

def generate_random_numbers(count=10, start=1, end=100):
    return [random.randint(start, end) for _ in range(count)]

def get_lucky_number(numbers):
    return random.choice(numbers)

def calculate_statistics(numbers):
    return {
        "avg": mean(numbers),
        "stdev": stdev(numbers),
        "max": max(numbers),
        "min": min(numbers),
        "sqrt_sum": math.sqrt(sum(numbers))
    }

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def feladat_01():
    # TODO: függvények hívása is_prime... stb
    pass



def days_until_birthday(month, day):
    today = date.today()
    current_year = today.year

    try:
        birthday = date(current_year, month, day)
    except ValueError:
        print("Hibás dátum")
        return -1

    if birthday < today:
        birthday = date(current_year + 1, month, day)

    return (birthday - today).days

def feladat_02():
    try:
        month = int(input("Hónap: "))
        day = int(input("Nap: "))
        days_left = days_until_birthday(month, day)
        if days_left >= 0: # XXX: == 0 születésnap => 1 ...
            print(f'n{days_left} nap hátra a születésnapig')
    except ValueError:
        print("nem szám... nem jó")


def feladat_03():
    angle_deg = random.radint(0, 360)
    angle_rad = math.radians(angle_deg)
    func = random.choice(["sin", "cos"])

    correct = math.sin(angle_rad) if func == "sin" else math.cos(angle_rad)

    print(f"mennyi a {func}({angle_rad})")

    try:
        user_input = float(input("válasz: "))
        diff = abs(user_input - correct)
        if diff < 0.01:
            print("helyes tipp")
        else:
            print(f"nem pontos: {correct:.4f}")
    except ValueError:
        print("nem szám")


def feladat_04():
    def generate_random_time():
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)

        return datetime.combine(date.today(), datetime.min.time()) + timedelta(hours=hour, minutes=minute)

    time1 = generate_random_time()
    time2 = generate_random_time()
    start, end = sorted([time1, time2])

    delta = end - start
    hours, remainder = divmod(delta.seconds, 3600)
    minutes = remainder // 60

    print(f"véletlen időpontok: 1.{start.time()} \n2.{start.time()}\nkülönbség h:{hours} m:{minutes}")


def main_menu():
    while True:
        # TODO: ...
        print("1. szerencseszám 01_feladat\n2. szülinap\n3.")

        choice = input("1-4")

        if choice == '1':
            feladat_01()
        elif choice == '2':
            feladat_02
        else:
            pass


def main():
    main_menu()


main()