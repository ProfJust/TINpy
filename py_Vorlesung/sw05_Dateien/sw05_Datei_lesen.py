import os

# Python sucht das File im aktuellen Arbeitsordner, 
# nicht unbedingt im Ordner des Skripts.
# ==> In den Arbeitsordner wechseln 
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open("ingenieurlied.txt", "r") as f:
    inhalt = f.read()  # gesamten Inhalt lesen
    print(inhalt)
