from datetime import date, timedelta

# aktuelles Datum ausgeben
heute = date.today()
print("Heutiges Datum:", heute)

heilig_abend = date(heute.year, 12, 24)

# Falls heilig_abend dieses Jahr schon vorbei ist, nimm nächstes Jahr
if heilig_abend < heute:
    heilig_abend = date(heute.year + 1, 12, 24)

tage_bis_heilig_abend = (heilig_abend - heute).days
print("Tage bis Heilig Abend:", tage_bis_heilig_abend)

