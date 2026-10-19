def abstand_pruefen(abstand):
    if abstand < 20:
        return "Achtung: Hindernis!"
    else:
        return "Abstand ist sicher"


print(abstand_pruefen(15))
print(abstand_pruefen(25))
print(abstand_pruefen(10))