"""
Docstring für py_Game.whisper_sw02_turtlegrafik

Codebeispiel für Whisper, das die Turtle in der Turtlegrafik mit den Befehlen "left", "right", "stop" .... steuert.

left“ / „right“: Drehen + vorwärts

„go“, "forward": Geradeaus fahren

"backward" : Rückwärts

„slower“: Langsamer

„faster“: Schneller

„stop“: Anhalten

„quit“: Programm beenden
"""



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

    current_dir = None      # "left", "right", "go", None/stop
    step = 5                # Schrittweite
    turn_angle = 5         # Drehwinkel

    def process_command(cmd):
        nonlocal current_dir, step
        cmd = cmd.lower().strip()
        print(f"Verarbeite Kommando: {cmd}")

        if "left" in cmd:
            current_dir = "left"
        elif "right" in cmd:
            current_dir = "right"
        elif "go" in cmd:
            current_dir = "go"
        elif "backward" in cmd:
            current_dir = "back"
        elif "forward" in cmd:
            current_dir = "go"
        elif "stop" in cmd:
            current_dir = None
        elif "slower" in cmd:
            step = max(1, step - 2)   # minimaler Schritt
            print(f"Geschwindigkeit: langsam (step={step})")
        elif "faster" in cmd:
            step = step + 2
            print(f"Geschwindigkeit: schnell (step={step})")

    # Turtle-Hauptloop
    while running:
        # neue Kommandos aus der Queue holen
        try:
            cmd = command_queue.get_nowait()
            process_command(cmd)
        except queue.Empty:
            pass

        # Bewegung entsprechend aktuellem Status
        if current_dir == "left":
            t.left(turn_angle)
            t.forward(step)
        elif current_dir == "right":
            t.right(turn_angle)
            t.forward(step)
        elif current_dir == "go":
            t.forward(step)
        elif current_dir == "back":
            t.backward(step)
        # bei stop: nichts machen

        screen.update()
        time.sleep(0.1)

    turtle.bye()

# ---------- Audioaufnahme & Whisper ----------
def record_audio(duration=3, samplerate=16000):
    print("Sprich jetzt ... (left/right/go/slow/fast/stop/quit)")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate,
                   channels=1, dtype="float32")
    sd.wait()
    print("Aufnahme beendet.")
    # in 16-bit ints umwandeln
    audio = (audio * 32767).astype(np.int16).flatten()
    return audio

def whisper_thread():
    global running
    model = whisper.load_model("base")  # ggf. "tiny", "small" etc.

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

        if "quit" in text.lower():
            running = False
            break

# ---------- Hauptprogramm ----------
if __name__ == "__main__":
    t_thread = threading.Thread(target=turtle_thread, daemon=True)
    t_thread.start()

    try:
        whisper_thread()
    except KeyboardInterrupt:
        running = False

    t_thread.join()
