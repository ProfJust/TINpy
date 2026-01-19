# pip install pyttsx3 
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
for i, v in enumerate(voices):
    print(i, v.id)  # zum Ausprobieren, welche Stimmen existieren

    """ bei mir mit Windows 11:
    0 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0
    1 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
    """

# z.B. erste Stimme wählen
engine.setProperty("voice", voices[1].id)

engine.say("Oh Hello, this is an english Text.")
engine.runAndWait()

