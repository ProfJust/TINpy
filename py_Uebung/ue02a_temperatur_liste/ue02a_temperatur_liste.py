import matplotlib.pyplot as plt
# ggf. > pip install matplotlib  
# oder python -m pip install matplotlib


temperaturen = [22, 24, 27, 31, 36, 42, 47, 51, 54, 56]

print(temperaturen)

print("Temperaturwerte: ")
for t in temperaturen:
    print(f" Wert {t:3d} °C")

print("Anzahl der Werte in Liste: ", len(temperaturen))
print("Erster Wert in der Liste: ", temperaturen[0])

temperaturen.append(44)
print("Nach append", temperaturen)
print("Letzter Wert in der Liste: ", temperaturen[9])

print("Letzter Wert in der Liste: ", temperaturen[len(temperaturen)-1])
print("Letzter Wert in der Liste: ", temperaturen[-1])  # letzte Wert der Liste

# Plot 
plt.xlabel("Index")
plt.ylabel("°C")
plt.title(" Temperatur eines Motors")
plt.grid()
plt.plot(temperaturen)
plt.show()