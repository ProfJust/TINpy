from astral import LocationInfo  # ggf. pip3 install astral  https://sffjunkie.github.io/astral/
from astral.sun import sun
from astral import moon
import datetime

city = LocationInfo(name="Regensburg", region="Germany", timezone="Europe/Berlin", latitude=51.83914, longitude=6.65332)

# WHS Bocholt 51.8391405400251, 6.6533183867373875

c_data = sun(city.observer)

print("Sonnenaufgang: " + str(c_data["sunrise"]))
print("Sonnenuntergang: " + str(c_data["sunset"]))
print("Morgendämmerung: " + str(c_data["dawn"]))
print("Abenddämmerung: " + str(c_data["dusk"]))


phase = moon.phase(datetime.date(2026, 6, 2))
print(phase)                  

"""
moon.phase() sagt dir, wie viele „Tage seit Neumond“ vergangen sind; über die Intervalle kannst du daraus eine der klassischen vier Phasen ableiten.

moon.phase() (genauer: astral.moon.phase(date)) gibt dir eine Zahl zurück, die den Mondphasen‑Zyklus von Neumond bis kurz vor den nächsten Neumond beschreibt.
Rückgabewert ist ein float im Bereich etwa 0 bis 27.99 für das angegebene Datum.
Das entspricht der „Mondalter“ in Tagen innerhalb eines synodischen Monats (ca. 29,53 Tage).

Typische Einteilung (laut Astral‑Doku):

0 .. 6.99 → Neumond‑Phase (neuer Mond, zunehmende schmale Sichel)
7 .. 13.99 → Erstes Viertel (zunehmender Halbmond)
14 .. 20.99 → Vollmond‑Phase
21 .. 27.99 → Letztes Viertel (abnehmender Halbmond bis kurz vor Neumond)

Example http://moongazer.x10.mx/website/astronomy/moon-phases/
"""