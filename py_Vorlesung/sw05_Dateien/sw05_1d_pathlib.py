from pathlib import Path

# Ordner, in dem dieses Skript liegt
script_dir = Path(__file__).resolve().parent
# Dateipfad zusammenfügen 
dateipfad = script_dir / "ingenieurlied.txt"
print(dateipfad)
text = dateipfad.read_text(encoding="utf-8")
# print(text)

p = script_dir / "log.txt"
text = p.read_text()
print(text)
p.write





# p = Path("texte", "ingenieurslied.txt")
# if p.exists():
#     text = p.read_text(encoding="utf-8")
# else:
#     print(f"Pfad {p} nicht gefunden")
