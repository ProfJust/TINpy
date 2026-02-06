from datetime import date, timedelta
from astral import moon

def first_full_moon_after_march_21(year: int) -> date:
    """Ersten Vollmond nach dem 21.3. des gegebenen Jahres finden."""
    # Startdatum: 21. März
    d = date(year, 3, 21)

    # Ab 21.3. tagweise vorgehen, bis wir das erste Datum
    # im Vollmond-Bereich (14–20.99) der Astral-Phase finden
    while True:
        phase = moon.phase(d)
        # Vollmondbereich laut Astral-Dokumentation
        if 14.0 <= phase <= 20.99:
            return d
        d += timedelta(days=1)

def first_sunday_after(day: date) -> date:
    """Ersten Sonntag NACH einem gegebenen Datum finden."""
    # weekday(): Montag=0, ..., Sonntag=6
    weekday = day.weekday()
    days_until_sunday = (6 - weekday) % 7
    # "nach" heißt: mindestens 1 Tag später.
    if days_until_sunday == 0:
        days_until_sunday = 7
    return day + timedelta(days=days_until_sunday)

def easter_like_date_for_year(year: int) -> tuple[date, date]:
    """Gibt (Vollmonddatum, erster Sonntag danach) für das Jahr zurück."""
    full_moon = first_full_moon_after_march_21(year)
    sunday_after = first_sunday_after(full_moon)
    return full_moon, sunday_after

if __name__ == "__main__":
    current_year = date.today().year
    full_moon_date, sunday_date = easter_like_date_for_year(current_year)

    print(f"Aktuelles Jahr: {current_year}")
    print(f"Erster Vollmond nach dem 21.3.: {full_moon_date}")
    print(f"Erster Sonntag danach:         {sunday_date}")
