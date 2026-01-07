# pip install openai-whisper sounddevice numpy
"""Hinweise:

Spracheingabe: Kommandos klar auf Englisch sprechen: „left“, „right“, „stop“, „quit“.

Je nach Mikrofonqualität evtl. duration oder Modellgröße anpassen; 
für schnellere Reaktion kleinere Modelle wie tiny oder small wählen."""

import threading  
import queue
import time
import turtle
import sounddevice as sd
import numpy as np
import whisper

# ---------- Globale Zustandsvariablen ----------
command_queue = queue.Queue()
running = True

# ---------- Turtle-Thread ----------
def turtle_thread():
    screen = turtle.Screen()
    screen.title("Whisper Turtle Control")

    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(1)

    current_dir = None  # "left", "right", None/stop

    def process_command(cmd):
        nonlocal current_dir
        cmd = cmd.lower().strip()
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
            process_command(cmd)
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
    print("Sprich jetzt ...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate,
                   channels=1, dtype="float32")
    sd.wait()
    print("Aufnahme beendet.")
    # in 16-bit ints umwandeln für Whisper
    audio = (audio * 32767).astype(np.int16).flatten()
    return audio

def whisper_thread():
    global running
    model = whisper.load_model("base")  # Modellgröße nach Bedarf ändern

    while running:
        audio = record_audio(duration=3)
        # Whisper erwartet float32 im Bereich -1..1
        audio_float = audio.astype(np.float32) / 32768.0

        print("Transkribiere ...")
        result = model.transcribe(audio_float, language="en")
        text = result.get("text", "").strip()
        if text:
            print(f"Erkannt: '{text}'")
            command_queue.put(text)

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
