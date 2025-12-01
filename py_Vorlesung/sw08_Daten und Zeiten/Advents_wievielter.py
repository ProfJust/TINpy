import datetime

def advent_sundays(year):
    # Weihnachten im aktuellen Jahr
    christmas = datetime.date(year, 12, 25)

    # Wochentag von Weihnachten (Montag=0 ... Sonntag=6)
    weekday = christmas.weekday()

    # Wir wollen den vorhergehenden Sonntag finden
    # (wenn Weihnachten Sonntag ist → 0 Tage zurück)
    days_back_to_sunday = (weekday + 1) % 7

    # 4. Advent: letzter Sonntag vor Weihnachten
    fourth_advent = christmas - datetime.timedelta(days=days_back_to_sunday)

    # Die anderen Adventssonntage liegen jeweils 7 Tage davor
    third_advent  = fourth_advent - datetime.timedelta(days=7)
    second_advent = third_advent  - datetime.timedelta(days=7)
    first_advent  = second_advent - datetime.timedelta(days=7)

    return first_advent, second_advent, third_advent, fourth_advent


# Beispiel:
year = 2025
advents = advent_sundays(year)
names = ["1. Advent", "2. Advent", "3. Advent", "4. Advent"]

for name, date in zip(names, advents):
    print(f"{name}: {date}")
