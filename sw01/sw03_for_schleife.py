# ran[] = range(5)
# print(ran[])
# for i in range(5):
#     print(i, end=' ')

# print("\n")
# for letter in 'Gadsby':
#     print(letter, end=' ')  

# print("\n")
# for letter in "Geadsby":
#     if letter == 'E' or letter == 'e':
#         print('This word has an "e"')   

# def has_e(word):
#     for letter in word:
#         if letter == 'E' or letter == 'e':
#             return True  # Verlasse Funktion
#     return False

def has_e(word):
    if 'E' in word or 'e' in word:
        return True
    else:
        return False
    
def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False
    
# # main    
# value = has_e('Gadsby')
# print(value)

# value =has_e('Emma')
# print(value)


file_object = open('sw01/deutscher_Text.txt')
line_cntr = 0 
e_cntr = 0

for line in file_object:
    zeile = line.strip() # entfern /n
    print(zeile)
    line_cntr +=1 
    if has_e(zeile):
        e_cntr +=1

print("Das ware",line_cntr, "Zeilen")
print("und  ",e_cntr, " Zeilen mit E")
value = uses_any(zeile,'ea') # kommen die einzelnen Buchstaben vor?
print(value)