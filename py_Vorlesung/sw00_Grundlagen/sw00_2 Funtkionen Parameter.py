def abstand_pruefen(abstand):
    if abstand < 20:
        print("Achtung: Hindernis!")
    else:
        print("Abstand ist sicher")


abstand_pruefen(15)
abstand_pruefen(25)
abstand_pruefen(10)