# pip install pyttsx3
import pyttsx3

# Engine initialisieren
engine = pyttsx3.init()

# Optional: Eigenschaften setzen
engine.setProperty("rate", 150)    # Sprechgeschwindigkeit
engine.setProperty("volume", 0.9)  # Lautstärke (0.0 bis 1.0)

text = "Hallo, dies ist ein Text-zu-Sprache Beispiel mit Peiton."
# text = "Oh hello, this is an english text."

engine.say(text)       # Text in die Warteschlange legen
engine.runAndWait()    # Ausgabe abspielen und warten, bis fertig


