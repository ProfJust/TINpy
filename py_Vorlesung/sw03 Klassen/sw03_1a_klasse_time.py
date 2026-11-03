# [DOW25] Kapitel 14 Klassen und Funktionen

class Time:
    """Represents a time of day."""  # Docstring, der den Zweck der Klasse erklärt


if __name__ == '__main__':
    # Objekt der Klasse Time() anlegen (Instanzieren)
    lunch = Time() 

    print(type(lunch))  # => <class '__main__.Time'>

    # Attribute an Objekt anhängen
    lunch.hour = 11
    lunch.minute = 59
    lunch.second = 1
    print("Lunch Time", lunch.hour,":", lunch.minute,":", lunch.second)
    
    # Format String
    # --------------------
    # Formatspezifizierer 02d bewirkt, dass minute und second 
    # mit mindestens zwei Ziffern (2d) und 
    # bei Bedarf mit einer führenden Null (0) ausgegeben werden 
    fstr = f'{lunch.hour}:{lunch.minute:02d}:{lunch.second:02d}'
    print(fstr)