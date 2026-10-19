
# Ersatz für eine do...while-Schleife

cntr = 12
while True:  # Prüfung der Kopfbedingung ausschalten => do
    print("Loop ", cntr)
    cntr -= 1
    if cntr < 10:  # Prüfe Bedingung am Fuss der Schleife while(Bdg)
        print("Beende Schleife da Bedingung erfüllt")
        break

print("Ende der Schleife")
