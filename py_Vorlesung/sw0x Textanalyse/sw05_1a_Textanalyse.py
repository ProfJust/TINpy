# Download Text unter https://www.gutenberg.org/cache/epub/43/pg43.txt
# https://allendowney.github.io/ThinkPython/

import os
# print("Current working directory:", os.getcwd())
import unicodedata

filename = 'dr_jekyll.txt'
# Python sucht das File im aktuellen Arbeitsordner, nicht unbedingt im Ordner des Skripts. 
# => Da der Text im selben Verzeichnis liegt, den absoluten Pfad erzeugen
#
# __file__: Eine spezielle Variable in Python, die den vollständigen Pfad der aktuellen Skriptdatei enthält # 
# abspath() Wandelt den Pfad in einen absoluten Pfad um (falls er relativ war).
# os.path.dirname(...): Gibt nur den Ordner zurück, in dem das Skript liegt (ohne den Dateinamen).
# Ergebnis: script_dir enthält den vollständigen Pfad zum Ordner, in dem dein Skript liegt.
script_dir = os.path.dirname(os.path.abspath(__file__))

# chdir() wechselt das aktuelle Arbeitsverzeichnis (Current Working Directory) 
os.chdir(script_dir)

def split_line(line):
    """ersetzt Ge-dankenstriche durch Leerzeichen, teilt den String 
    und gibt die entstandene Liste zurück"""
    return line.replace('–', ' ').split()

try:
    unique_words = {}  # leeres Dictionary
    with open(filename, 'r', encoding='utf-8',  errors='ignore') as file:
        for line in file:
            seq = line.split()
            for word in seq:
                unique_words[word] = 1
        # Jedes Mal, wenn ein neues Wort gefunden wird, wird es als Schlüssel (word) ins Dictionary eingefügt.
        # Der Wert (1) ist hier nur ein Platzhalter – es geht nur darum, ob das Wort schon im Dictionary ist.
        # Effekt: Da ein Dictionary keine doppelten Schlüssel erlaubt, wird jedes Wort nur einmal gespeichert, egal wie oft es in der Datei vorkommt.
        # ggf. Ende vom Text ab Zeile 2578 löschen wenn Number of unique words größer 6089 ist wie hier:
        #       Number of unique words: 6710
        #       ['(www.gutenberg.org),', '(trademark/copyright)', 'www.gutenberg.org/contact', 'www.gutenberg.org/donate.', 'www.gutenberg.org/license.']
    print("Number of unique words:", len(unique_words))
    print(sorted(unique_words, key=len)[-5:])

    print(unicodedata.category('A'))  # Lu  => Letter uppercase
    print(unicodedata.category('.'))  # Po  => Punctuation others

    punc_marks = {}
    for line in filename:
        for char in line:
            category = unicodedata.category(char)
            print(category)
            if category.startswith('P'):
                punc_marks[char] = 1
                punctuation = ''.join(punc_marks) 
                print(punctuation)  
    
    

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found in {os.getcwd()}")
except UnicodeDecodeError:
    print(f"Error: Could not decode the file '{filename}'. Try using a different encoding.")
