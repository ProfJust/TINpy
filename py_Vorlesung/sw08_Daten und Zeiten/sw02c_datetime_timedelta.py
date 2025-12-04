from datetime import date, timedelta

heute = date.today()
# Weihnachten dieses Jahr (Heilig Abend)
weihnachten = date(heute.year, 12, 24)

# Differenz als timedelta
# diff: timedelta
diff = weihnachten - heute

print("Heute:", heute)
print("Nächstes Weihnachten:", weihnachten)
print("Tage bis Weihnachten:", diff.days)