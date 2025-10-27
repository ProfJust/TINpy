liste = ['spam', 2.0, 5, [10, 20, 12, 'liste'], 56] # Liste anlegen

for i in range(len(liste)):
    elemente_in_liste = len(liste)
    element = liste[i]
    print("Liste [",i,"]", element)

print(" Es sind ",elemente_in_liste," Elemente in der Liste")
for element in liste:
    print(element)


letters = ['a', 'b', 'c', 'd']
w = letters[1:]
w2 = list(letters)
print(w)
print(w2)