liste_temperatur = [22.5, 23.1, 21.9, 21.9, 24.0, 22.8] # Anlegen einer Liste mit []
# print(liste_temperatur)
print(liste_temperatur[0])  # erstes Element der Liste
print(liste_temperatur[4],"\n")
print('Letztes Element der Liste mit [-1]: ',liste_temperatur[-1],"\n")
# for i in range(len(liste_temperatur)):   # index 0..4   C-Style
#     print(liste_temperatur[i])
  
# print("\n")
for element in liste_temperatur:  # Python Style
    print(element)

summe = sum(liste_temperatur) # werte_addieren
numb_of_el = len(liste_temperatur)
durchschnitt = summe / numb_of_el
print("Durchschnitt",durchschnitt)

# liste_temperatur[len(liste_temperatur)] = 6.66
liste_temperatur.append(23.4)  # An Liste anhängen, mit Speicherplatzreservierung
print(liste_temperatur)

minimum = min(liste_temperatur)
print('Mnimum: ',minimum)

# 6. Niedrigster Wert entfernen
liste_temperatur.remove(min(liste_temperatur))
print("Min gelöscht", liste_temperatur)
print(" pop(2)", liste_temperatur.pop(2))

liste_temperatur.sort(reverse=False)  # Sortieren Auf- oder Absteigend
print(liste_temperatur)


temperaturen_gerundet = [round(wert) for wert in liste_temperatur] # List Comprehension
print(temperaturen_gerundet)

for i in range(len(liste_temperatur)):  # C-Style
    liste_temperatur[i] = round(liste_temperatur[i])

print(liste_temperatur)

hoechster = max(liste_temperatur)
kleinster = min(liste_temperatur)
print('Differen hoechtser, kleinster', abs(hoechster-kleinster))

temperaturdifferenz = max(liste_temperatur) - min(liste_temperatur)
print("Temperaturdifferenz:", round(temperaturdifferenz, 1), "°C")



