from pathlib import Path

# Ordner, in dem dieses Skript liegt
script_dir = Path(__file__).resolve().parent
# Dateipfad zusammenfügen 
dateipfad = script_dir / "ingenieurlied.txt"
print(dateipfad)
text = dateipfad.read_text(encoding="utf-8")
print(text)

p = script_dir / "log.txt"
text = p.read_text()
print(text)
p.write_text("Neuer Text im Logfile.\n")  
print("path: ",p)
print("name: ", p.name) # 
print("stem: ", p.stem) # 
print("suffix: ", p.suffix) # '.pdf'
print("parent: ", p.parent) # '/home/olaf/berichte' 
print("\n ---------- \n")
# globale Suche nach Dateien => GREAT !!
for f in Path(".").glob("config.yaml"):
    print(f)
    if f.exists():
        text = f.read_text(encoding="utf-8")    
        print(text)    
    else:
        print(f"Pfad {f} nicht gefunden")


