# 1. Messdaten als 2D-Liste speichern
Liste_temp = [
    [22.5, 23.1, 21.9, 24.0, 22.8],  # Zeit 0s    Zeile[0]
    [22.7, 23.4, 22.2, 23.9, 23.0],  # Zeit 20s   Zeile[1]
    [22.6, 23.2, 22.0, 24.2, 23.1],  # Zeit 40s
    [22.8, 23.3, 22.1, 30.0, 23.9],  # Zeit 60s
]

liste_spalte = [ liste[0] for liste in Liste_temp]
print("Splate 0", liste_spalte)

liste_durchschnitt = [ sum(liste)/len(liste) for liste in Liste_temp]
print("Durchschnitt", liste_durchschnitt)

Liste_temp.append([22.9, 23.5, 22.3,24.1, 23.3])
print(Liste_temp)

hoechste_temp_ever =  float('-inf')  # größter negativer Wert 
ht_index_sensor =    -1
ht_index_zeit = -1
for zeit_index, liste_zeile in enumerate(Liste_temp):  # Äußere Schleife
    # print(zeit_index, liste_zeile )
    for sensor_index, wert in enumerate(liste_zeile):  # Innere Schleife
        # print(sensor_index,wert)
        if wert > hoechste_temp_ever:
            hoechste_temp_ever = wert
            ht_index_sensor  = sensor_index
            ht_index_zeit = zeit_index

print('hoechste_temp_ever  ', hoechste_temp_ever, 
      'an Sensor' , ht_index_sensor, 
      ' Zeit sec', ht_index_zeit*20)