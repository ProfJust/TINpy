import os

# Python sucht das File im aktuellen Arbeitsordner, 
# nicht unbedingt im Ordner des Skripts.
# ==> In den Arbeitsordner wechseln 
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open("output.txt", "w") as f:
    f.write("Hallo Welt!\n")


with open("log.txt", "a") as f:
    f.write("Neue Logzeile\n")

if os.path.exists("bild.jpg"):
    print("Datei gefunden")
    with open("bild.jpg", "rb") as quelle:
        with open("kopie.jpg", "wb") as ziel:
            daten = quelle.read()
            ziel.write(daten)
else:
    print("Datei nicht gefunden")

print(os.listdir("."))