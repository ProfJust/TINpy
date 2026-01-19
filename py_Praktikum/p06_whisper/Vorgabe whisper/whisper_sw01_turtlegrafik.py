# ggf. pip install openai-whisper sounddevice numpy
"""Hinweise:

Spracheingabe: Kommandos klar auf Englisch sprechen: „left“, „right“, „stop“, „quit“.

Je nach Mikrofonqualität evtl. duration oder Modellgröße anpassen; 
für schnellere Reaktion kleinere Modelle wie tiny oder small wählen."""

import threading   # Parallele Prozesse 
import queue       # Datenspeicher FiFo
import time 
import turtle
import sounddevice as sd  # Audioaufnahme
import numpy as np   # Signalaufbereitung
import whisper  # Speech‑to‑Text‑Transkription

# ---------- Globale Zustandsvariablen ----------
command_queue = queue.Queue()   # Datenspeicher zum Austausch der Daten zwischen Prozessen
running = True  # globaler Flag, der beide Threads steuert und beim Beenden (z. B. „quit“) auf False gesetzt wird


# ---------- Turtle-Thread ----------
def turtle_thread():
    """
        erstellt ein Turtle‑Fenster,
        initialisiert eine Turtle und 
        steuert Geschwindigkeit und Steuerparameter (step, turn_angle)
    """
    screen = turtle.Screen()
    screen.title("TINpy - Whisper Turtle Control")

    t = turtle.Turtle()
    t.shape("turtle")   # Aussehen der Turtle: 'arrow', 'circle', 'classic', 'square', 'triangle', and 'turtle'
    t.speed(1)          # The speed range is 0-10 1 (slowest) → Slowest speed

    current_dir = None  # Fahrtrichtung "left", "right", None/stop

    def process_command(cmd):  # Fahrtkommando bestimmen
        nonlocal current_dir  # variable should not belong to the inner function
        cmd = cmd.lower().strip()  # cmd in Kleinbuchstaben wandeln und Leerzeichen entfernen
        if "left" in cmd:
            current_dir = "left"
        elif "right" in cmd:
            current_dir = "right"
        elif "stop" in cmd:
            current_dir = None

    # Turtle-Hauptloop
    while running:
        # neue Kommandos aus der Queue holen
        try:
            cmd = command_queue.get_nowait()  
            print(f"Empfangenes Kommando: {cmd}")
            process_command(cmd)  # Fahrtkommando bestimmen
        except queue.Empty:
            pass

        # Bewegung entsprechend aktuellem Status
        if current_dir == "left":
            t.left(10)
            t.forward(5)
        elif current_dir == "right":
            t.right(10)
            t.forward(5)
        # bei stop: nichts machen

        screen.update()
        time.sleep(0.1)

    turtle.bye()


# ---------- Audioaufnahme & Whisper ----------
def record_audio(duration=3, samplerate=16000):
    """ nimmt für duration Sekunden Mono‑Audio mit 16 kHz auf,
        gibt Hinweise im Terminal aus und
        skaliert das Float‑Signal in 16‑Bit‑Integer"""
    print("Sprich jetzt ...")
    # sounddevice: Audio vom Mikrofon aufnehmen und in ein NumPy‑Array wandeln 
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate,
                   channels=1, dtype="float32")
     # Die Funktion kehrt sofort zurück; die eigentliche Aufnahme läuft im Hintergrund weiter,
     # bis sd.wait() aufgerufen wird, um zu warten, bis sie fertig ist.
    sd.wait() 
    print("Aufnahme beendet.")
    # in 16-bit ints umwandeln für Whisper
    audio = (audio * 32767).astype(np.int16).flatten()
    return audio


def whisper_thread():
    global running
    model = whisper.load_model("base")  # Modellgröße nach Bedarf ändern

    while running:
        audio = record_audio(duration=2)  # Aufnahme Audio 
        # Whisper erwartet float32 im Bereich -1..1
        audio_float = audio.astype(np.float32) / 32768.0

        print("Transkribiere ...")
        result = model.transcribe(audio_float, language="en")
        text = result.get("text", "").strip()
        if text:
            print(f"Erkannt: '{text}'")
            command_queue.put(text)  # Gewonnener Text als Kommando in den Pufferpspeicher

        # Beenden, wenn explizit "quit" gesagt wird
        if "quit" in text.lower():
            running = False
            break


# ---------- Hauptprogramm ----------
if __name__ == "__main__":
    # Turtle in separatem Thread starten
    t_thread = threading.Thread(target=turtle_thread, daemon=True)
    t_thread.start()

    # Whisper-/Spracherkennung im Hauptthread
    try:
        whisper_thread()
    except KeyboardInterrupt:
        running = False

    t_thread.join()
